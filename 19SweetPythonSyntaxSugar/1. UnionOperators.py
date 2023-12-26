# This Python file uses the following encoding: utf-8
import sys

# https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
# 1. Union Operators: The Most Elegant Way To Merge Python Dictionaries


class Sugar:
    def __init__(self):
        cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
        cities_uk = {'London': 'UK', 'Birmingham': 'UK'}
        cities_jp = {'Tokyo': 'JP'}

        cities = {}

        for city_dict in [cities_us, cities_uk, cities_jp]:
            for city, country in city_dict.items():
                cities[city] = country

        print(cities)
        # {'New York City': 'US', 'Los Angeles': 'US', 'London': 'UK', 'Birmingham': 'UK', 'Tokyo': 'JP'}

    def elegant(self):
        cities_us = {'New York City': 'US', 'Los Angeles': 'US'}
        cities_uk = {'London': 'UK', 'Birmingham': 'UK'}
        cities_jp = {'Tokyo': 'JP'}

        cities = cities_us | cities_uk | cities_jp

        print(cities)

        cities_us |= cities_uk | cities_jp
        print(cities_us)


if __name__ == "__main__":
    sugar = Sugar()
    sugar.elegant()
