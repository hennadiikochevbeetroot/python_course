class Fibonacci:
    def __init__(self, threshold: int = 20):
        self.__generated_threshold = threshold

    def __iter__(self):
        self.__current = 0
        self.__next = 1
        self.__generated = 0
        return self

    def __next__(self):
        if self.__generated < self.__generated_threshold:
            self.__generated += 1
            current_fibonacci = self.__current
            self.__current, self.__next = self.__next, self.__current + self.__next
            return current_fibonacci

        raise StopIteration


for idx, fib in enumerate(Fibonacci(15), 1):
    print(f'Fibonacci number {idx}: {fib}')
