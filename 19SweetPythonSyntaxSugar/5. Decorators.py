# This Python file uses the following encoding: utf-8
import sys


# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 5. Decorators in Python: A Way To Modularize Functionalities and Separate Concerns


class Sugar:
    def __init__(self):
        ...

    def elegant(self):
        ...


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = None

    def set_nickname(self, name):
        self.nickname = name

    @staticmethod
    def suitable_age(age):
        return 6 <= age <= 70


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()

    print(Student.suitable_age(99))  # False
    print(Student.suitable_age(27))  # True
    print(Student('yang', 'zhou').suitable_age(27))  # True
