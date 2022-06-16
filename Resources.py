class Resources:
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9
    money_left = 550

    def __repr__(self):
        return f'The coffee machine has:({self.water}, {self.milk}, {self.beans}, {self.disposable_cups}, {self.money_left}'

    def __str__(self):
        return f'\nThe coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n' \
               f'{self.beans} g of coffee beans\n{self.disposable_cups} disposable cups\n${self.money_left} of money\n'
