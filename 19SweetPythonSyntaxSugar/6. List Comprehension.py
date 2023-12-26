# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 6. List Comprehension: Make a List in One Line of Code


class Sugar:
    def __init__(self):
        Entrepreneurs = ["Yang", "Mark", "steve", "jack", "tom"]
        D1 = {index: name for index, name in enumerate(Entrepreneurs) if name[0].isupper()}
        print(D1)
        # {0: 'Yang', 1: 'Mark'}

    def elegant(self):
        Genius = ["Yang", "Tom", "Jerry", "Jack", "tom", "yang"]
        L1 = [name for name in Genius if name.startswith('Y')]
        L2 = [name for name in Genius if name.startswith('Y') or len(name) < 4]
        L3 = [name for name in Genius if len(name) < 4 and name.islower()]
        print(L1, L2, L3)
        # ['Yang'] ['Yang', 'Tom', 'tom'] ['tom']


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
