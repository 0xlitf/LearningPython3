# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 15. Swapping Two Variables Directly


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        a = 10
        b = 5
        print(a, b)
        a, b = b, a
        print(a, b)
        # 5 10


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
