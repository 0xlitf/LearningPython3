# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 10. Context Manager: Close Resources Automatically


class Sugar:
    def __init__(self):
        f = open("test.txt", 'w')
        f.write("Hi,Yang!")
        # some logic here
        f.close()

    def elegant(self):
        with open("test.txt", 'w') as f:
            f.write("Hi, Yang!")


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
