# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 18. Any() and All() Functions


class Sugar:
    def __init__(self):
        my_list = [3, 5, 7, 8, 11]
        all_odd = all(num % 2 == 1 for num in my_list)
        print(all_odd)
        # False

    def elegant(self):
        leaders = ['Yang', 'Elon', 'Sam', 'Tim']
        starts_with_Y = any(name.startswith('Y') for name in leaders)
        print(starts_with_Y)
        # True


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
