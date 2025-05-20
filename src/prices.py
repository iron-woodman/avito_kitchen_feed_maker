import random

class Price:
    stol_prices = []
    um_prices = []
    podokonnik_prices = []

    def __init__(self):
        self.kitchen_prices = [price for price in range(10000, 20000, 1000)]

    def get_price(self, product: str):
        """
        получить цену товара
        :return:
        """
        if product == 'kitchen':
            return random.choice(self.kitchen_prices)
