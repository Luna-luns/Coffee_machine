from Resources import Resources


class CoffeeTypes:
    ESPRESSO_WATER = 250
    ESPRESSO_MILK = 0
    ESPRESSO_BEANS = 16
    ESPRESSO_COSTS = 4
    LATTE_WATER = 350
    LATTE_MILK = 75
    LATTE_BEANS = 20
    LATTE_COSTS = 7
    CAPPUCCINO_WATER = 200
    CAPPUCCINO_MILK = 100
    CAPPUCCINO_BEANS = 12
    CAPPUCCINO_COSTS = 6

    resources = Resources()
    _list = None

    def count_spent_resources(self, constant_water: int, constant_milk: int, constant_beans: int, constant_disposable_cups: int, constant_money_left: int, constant_costs: int):
        _water = self.resources.water - constant_water
        _milk = self.resources.milk - constant_milk
        _beans = self.resources.beans - constant_beans
        _disposable_cups = constant_disposable_cups - 1
        _money_left = constant_money_left + constant_costs
        _list = [_water, _milk, _beans, _disposable_cups, _money_left]
        self._list = _list

    def check_availability(self) -> str:
        _water, _milk, _beans, _disposable_cups, _money_left = self._list

        if _water >= 0 and _milk >= 0 and _beans >= 0 and _disposable_cups >= 0:
            self.resources.water, self.resources.milk, self.resources.beans, self.resources.disposable_cups, self.resources.money_left = _water, _milk, _beans, _disposable_cups, _money_left
            return 'I have enough resources, making you a coffee!' + '\n'

        elif _water < 0 <= _milk and _beans >= 0 and _disposable_cups >= 0:

            return 'Sorry, not enough water!' + '\n'

        elif _water >= 0 > _milk and _beans >= 0 and _disposable_cups >= 0:

            return 'Sorry, not enough milk!' + '\n'

        elif _water >= 0 > _beans and _milk >= 0 and _disposable_cups >= 0:

            return 'Sorry, not enough beans!' + '\n'

        elif _water >= 0 and _milk >= 0 and _disposable_cups < 0 <= _beans:

            return 'Sorry, not enough disposable_cups!' + '\n'
