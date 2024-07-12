
# Strings are in single or double quotes, no matter
a = 'string single quote'
b = "string double quote"
print(a, type(a))
print(b)
print()

# Escaping quotes
c = 'with \'single quote\' inside'
d = "with \"double quote\" inside"
print(c)
print(d)
print()

# Single inside of double and vice versa
c = "with 'single quote' inside"
d = 'with "double quote" inside'
print(c)
print(d)
print()

# Multiline strings
e = 'line1\
line2'
f = ('line1'
     'line2')
g = """
Really
multiline 
string
"""
print(e)
print(f)
print(g)
print()
