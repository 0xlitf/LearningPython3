# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 9. Use the “Enumerate” Method To Iterate Lists Elegantly


class Sugar:
    def __init__(self):
        # for (int i = 0; i < len_of_list; i++) {
        #     printf("%d %s\n", i, my_list[i]);
        # }
        ...

    def elegant(self):
        leaders = ["Warren", "Yang", "Tim", "Elon"]
        for i, v in enumerate(leaders):
            print(i, v)
        # 0 Warren
        # 1 Yang
        # 2 Tim
        # 3 Elon


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
