import random


class Title:
    kitchen_titles = []

    def __init__(self):
        self.kitchen_titles = self.load_titles('titles/kitchen.txt')

    def get_kitchen_title(self):
        """
        получить заголовок для умывальника
        :return:
        """
        return random.choice(self.kitchen_titles)

    def load_titles(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            return f.read().split('\n')
