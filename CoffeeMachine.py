from Resources import Resources
from CoffeeTypes import CoffeeTypes


class CoffeeMachine:
    # states
    WAIT_COMMAND = 'wait for command'
    WAIT_WATER = 'wait for water'
    WAIT_MILK = 'wait milk'
    WAIT_BEANS = 'wait beans'
    WAIT_CUPS = 'wait cups'
    WAIT_COFFEE_TYPE = 'wait for coffee type'

    state = WAIT_COMMAND
    resources = Resources()
    coffee_type = CoffeeTypes()

    def execute_command(self, command: str) -> str:
        if command == '1' and self.state == self.WAIT_COFFEE_TYPE:
            self.coffee_type.count_spent_resources(self.coffee_type.ESPRESSO_WATER, self.coffee_type.ESPRESSO_MILK, self.coffee_type.ESPRESSO_BEANS, self.resources.disposable_cups, self.resources.money_left, self.coffee_type.ESPRESSO_COSTS)
            answer = self.coffee_type.check_availability()
            self.resources = self.coffee_type.resources
            self.state = self.WAIT_COMMAND

            return answer

        if command == '2' and self.state == self.WAIT_COFFEE_TYPE:
            self.coffee_type.count_spent_resources(self.coffee_type.LATTE_WATER, self.coffee_type.LATTE_MILK, self.coffee_type.LATTE_BEANS, self.resources.disposable_cups, self.resources.money_left, self.coffee_type.LATTE_COSTS)
            answer = self.coffee_type.check_availability()
            self.resources = self.coffee_type.resources
            self.state = self.WAIT_COMMAND

            return answer

        if command == '3' and self.state == self.WAIT_COFFEE_TYPE:
            self.coffee_type.count_spent_resources(self.coffee_type.CAPPUCCINO_WATER, self.coffee_type.CAPPUCCINO_MILK, self.coffee_type.CAPPUCCINO_BEANS, self.resources.disposable_cups, self.resources.money_left, self.coffee_type.CAPPUCCINO_COSTS)
            answer = self.coffee_type.check_availability()
            self.resources = self.coffee_type.resources
            self.state = self.WAIT_COMMAND

            return answer

        if command == 'back' and self.state == self.WAIT_COFFEE_TYPE:
            self.state = self.WAIT_COMMAND
            return ''

        if self.state == self.WAIT_WATER:
            self.resources.water += int(command)
            self.state = self.WAIT_MILK

            return ''

        if self.state == self.WAIT_MILK:
            self.resources.milk += int(command)
            self.state = self.WAIT_BEANS

            return ''

        if self.state == self.WAIT_BEANS:
            self.resources.beans += int(command)
            self.state = self.WAIT_CUPS

            return ''

        if self.state == self.WAIT_CUPS:
            self.resources.disposable_cups += int(command)
            self.state = self.WAIT_COMMAND

            return ' '

        if command == 'remaining' and self.state == self.WAIT_COMMAND:
            return self.resources.__str__()

        if command == 'fill' and self.state == self.WAIT_COMMAND:
            self.state = self.WAIT_WATER
            return ''

        if command == 'take' and self.state == self.WAIT_COMMAND:
            return self.take_money()

        if command == 'buy' and self.state == self.WAIT_COMMAND:
            self.state = self.WAIT_COFFEE_TYPE
            return ''

        if command == 'exit' and self.state == self.WAIT_COMMAND:
            exit()

    def take_money(self) -> str:
        money = self.resources.money_left
        self.resources.money_left = 0

        return f'\nI gave you ${money}\n'

    def get_state(self) -> str:
        return self.state
