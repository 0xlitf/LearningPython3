# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 8. Ternary Conditional Operators: Put If and Else Into One Line of Code


a = [1, 2]
b = [1, 2, 3]


class Sugar:
    def __init__(self):
        short_one = ''
        if len(a) < len(b):
            short_one = a
        else:
            short_one = b
        print(short_one)

    def elegant(self):
        short_one = a if len(a) < len(b) else b
        print(short_one)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
