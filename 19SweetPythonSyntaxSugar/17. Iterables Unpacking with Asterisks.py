# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 17. Iterables Unpacking with Asterisks


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        A = [1, 2, 3]
        B = (4, 5, 6)
        C = {7, 8, 9}
        L = [*A, *B, *C]
        print(L)
        print([A, B, C])
        # [1, 2, 3, 4, 5, 6, 8, 9, 7]


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
