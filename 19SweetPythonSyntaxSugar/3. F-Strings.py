# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 3. F-Strings: A Pythonic String Formatting Approach

from datetime import datetime


class Sugar:
    def __init__(self):
        ...

    def elegant(self):

        today = datetime.today()

        print(f"Today is {today}")
        # Today is 2023-03-22 21:52:29.623619

        print(f"Today is {today:%B %d, %Y}")
        # Today is March 22, 2023

        print(f"Today is {today:%m-%d-%Y}")
        # Today is 03-22-2023

        print(f"Today is {datetime.today()}")
        # Today is 2023-03-22 22:00:32.405462


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
