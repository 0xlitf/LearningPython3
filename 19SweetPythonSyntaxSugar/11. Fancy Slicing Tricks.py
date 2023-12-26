# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 11. Fancy Slicing Tricks for Python Lists


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        # a_list[start:end:step]
        # Reverse a list with a slicing trick
        a = [1, 2, 3, 4]
        print(a[::-1])
        # [4, 3, 2, 1]

        # Get a shallow copy of a list
        a = [1, 2, 3, 4, 5, 6]
        b = a[:]
        b[0] = 100
        print(b)
        print(a)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
