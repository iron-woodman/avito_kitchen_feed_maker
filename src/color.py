import random


class Color:
    colors_list = []

    def __init__(self):
        self.colors_list = self.load('data/colors.txt')

    def get_random(self):
        """
        получить цвет
        :return:
        """
        return random.choice(self.colors_list)

    def load(self, file):
       with open(file, 'r', encoding='utf-8-sig') as f:
           return f.read().split('\n')
