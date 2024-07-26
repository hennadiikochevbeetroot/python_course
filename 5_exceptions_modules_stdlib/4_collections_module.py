from collections import Counter, namedtuple, OrderedDict


animals = ['Cat', 'Dog', 'Horse', 'Dog']
animal_counter = Counter(animals)
print(animal_counter)

ordered_dict = OrderedDict()
ordered_dict['key1'] = 2
ordered_dict['key2'] = 4

for key in ordered_dict:
    print('Key: ', key)

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(f'Coordinates: X: {p.x}, Y: {p.y}')




