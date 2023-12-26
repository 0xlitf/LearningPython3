# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 16. Destructuring Assignments Tricks


class Sugar:
    def __init__(self):
        person = {'name': 'Yang', 'age': 30, 'location': 'Mars'}
        name, age, loc = person.values()
        print(name, age, loc)

    def elegant(self):
        person = {'name': 'Yang', 'age': 30, 'location': 'Mars'}
        name, *others = person.values()
        print(name, others)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
