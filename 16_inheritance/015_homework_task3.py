from dataclasses import dataclass
from enum import Enum


class ProductType(str, Enum):
    DRESS = 'Dress'
    SHIRT = 'Shirt'
    TROUSERS = 'Trousers'


@dataclass
class Product:
    id: int
    type: ProductType
    name: str
    price: float
    discount: int = 0
    amount_usual: int = 0
    amount_premium: int = 0

    def total_price_by_amount(self):
        return self.price_usual * self.amount_usual + self.price_premium * self.amount_premium

    @property
    def total_amount(self):
        return self.amount_premium + self.amount_usual

    @property
    def price_usual(self):
        return self.price * (100 - self.discount) / 100

    @property
    def price_premium(self):
        return self.price * 1.3 * (100 - self.discount) / 100

    def __str__(self) -> str:
        return (f'Product(type={self.type}, name={self.name}, price={self.price}, '
                f'discount={self.discount}, amount_usual={self.amount_usual}, amount_premium={self.amount_premium})')


class ProductStore:
    def __init__(self, products: list[Product]):
        self.products: list[Product] = products
        self.total_income: float = 0

    def add(self, product: Product, amount_premium: int):
        product.amount_premium += amount_premium

    def set_discount(self, identifier: ProductType | str, discount: int, identifier_type: str = 'name'):
        product: Product | None = None
        for product_search in self.products:
            if getattr(product_search, identifier_type) == identifier:
                product = product_search
                break

        if product is None:
            raise ValueError(f'Did not found product with {identifier_type} = {identifier}')

        product.discount = discount

    def sell_product(self, product_name: str, amount: int):
        product: Product | None = None
        for product_search in self.products:
            if product_search.name == product_name:
                product = product_search
                break

        if product is None:
            raise ValueError(f'Did not found product with name = {product_name}')

        if amount < product.amount_premium:
            product.amount_premium -= amount
            self.total_income += product.price_premium * amount

        elif amount < product.total_amount:
            premium_income = product.amount_premium * product.price_premium
            usual_income = (amount - product.amount_premium) * product.price_usual
            self.total_income += (premium_income + usual_income)

            product.amount_premium = 0
            product.amount_usual = product.total_amount - amount

        else:
            raise ValueError('Requested amount is greater than available')

    def get_total_income(self):
        return self.total_income

    def get_all_products_info(self) -> str:
        info = ''
        for product in self.products:
            info += str(product)
            info += '\n'

        return info


products: list[Product] = [
    Product(id=1, type=ProductType.DRESS, name='Evening Dress', price=234.56, amount_usual=10),
    Product(id=2, type=ProductType.TROUSERS, name='Morning Trousers', price=123.45, amount_usual=5),
]

product_store = ProductStore(products)

print('Current income:', product_store.get_total_income())

product_store.sell_product('Evening Dress', 3)
print('Current income:', product_store.get_total_income())
