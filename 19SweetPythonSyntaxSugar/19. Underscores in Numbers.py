# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 19. Underscores in Numbers


class Sugar:
    def __init__(self):
        a = 10000000000
        print(a)

    def elegant(self):
        a = 10_000_000_000
        print(a)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
