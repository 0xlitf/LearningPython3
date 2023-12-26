# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 13. Continuous Comparisons: A More Natural Way To Write If Conditions
a = 1

class Sugar:
    def __init__(self):
        ...
        # if (a > 1 & & a < 10){
        # // do somthing
        # }

    def elegant(self):
        if 1 < a < 10:
            ...


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
