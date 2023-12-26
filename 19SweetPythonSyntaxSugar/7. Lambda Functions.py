# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 7. Lambda Functions for Defining Small Anonymous Functions


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        leaders = ["Warren Buffett", "Yang Zhou", "Tim Cook", "Elon Musk"]
        leaders.sort(key=lambda x: len(x))
        print(leaders)
        # ['Tim Cook', 'Yang Zhou', 'Elon Musk', 'Warren Buffett']


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
