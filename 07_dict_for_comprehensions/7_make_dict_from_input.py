# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.

from collections import defaultdict


def sentence_to_dict(sentence: str) -> dict[str, int]:
    split_word = sentence.split()
    d = defaultdict(int)
    for key in split_word:
        d[key] += 1

    return dict(d)


if __name__ == '__main__':
    sentence = input("Please enter your input sentence - ")
    d = sentence_to_dict(sentence)
    print(d)
