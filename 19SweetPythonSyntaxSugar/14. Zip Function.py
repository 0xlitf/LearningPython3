# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 14. Zip Function: Combine Multiple Iterables Easily


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        id = [1, 2, 3, 4]
        leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']
        sex = ['male', 'male', 'male', 'male']
        record = zip(id, leaders, sex)

        print(list(record))
        # [(1, 'Elon Mask', 'male'), (2, 'Tim Cook', 'male'), (3, 'Bill Gates', 'male'), (4, 'Yang Zhou', 'male')]


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
