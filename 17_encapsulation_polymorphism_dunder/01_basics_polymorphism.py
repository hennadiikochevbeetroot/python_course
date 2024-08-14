# As we don't specify the types, then everything could be passed
# as parameter, as well as returned

def add(a, b):
    return a + b


# Polymorphism lets us call this same function with different parameter types

print(add(4, 5))
print(add(7.89, 56.43))
print(add('Hello,', 'World'))
print(add([1, 2, 3], [4, 5, 6]))
print(add((1, 2, 3), (4, 5, 6)))


# In static-typed languages like C++, Java, C#, such behaviour cannot be default.
# You would need to specify different functions for this, like:
# int add_int(int a, int b) {
#     return a + b;
# }
#
# float add_float(float a, float b) {
#     return a + b;
# }
#
# string add_string(string a, string b) {
#     return a + b;
# }

# Or use generics, which is a more complex topic
