
word_list = ['word1', 'word2', 'word3']
iterator = iter(word_list)

# lazy nature of iterators
print(next(iterator))
print(next(iterator))
print(next(iterator))

# if we try to continue calling next(),
# program will raise StopIteration exception

print(next(iterator))
