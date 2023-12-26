# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 12. Walrus Operator: Assignments within Expressions


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        # type at terminal
        print("please type at terminal, ended enter: ")
        while (line := input()) != "stop":
            print("typed: " + line)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
