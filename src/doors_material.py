import random


class DoorsMaterial:
    list = []

    def __init__(self):
        self.list = self.load_list('data/DoorsMaterial.txt')

    def get_random(self):
        """
        получить цвет
        :return:
        """
        return random.choice(self.list)

    def load_list(self, file):
       with open(file, 'r', encoding='utf-8-sig') as f:
           return f.read().split('\n')
