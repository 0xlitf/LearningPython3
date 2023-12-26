# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 2. Type Hints: Make Your Python Programs Type Safe
from typing import Final


class Sugar:
    def __init__(self):
        DATABASE = 'MySQL'

    def elegant(self):
        DATABASE: Final = "MySQL"
        print(DATABASE)
        DATABASE = "MangoDB"
        print(DATABASE)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
