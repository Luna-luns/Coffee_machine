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
DEFAULT_WATER = 400
DEFAULT_MILK = 540
DEFAULT_BEANS = 120
DEFAULT_DISPOSABLE_CUPS = 9
DEFAULT_COST = 550


def print_coffee_machine_data() -> None:

    print(f'The coffee machine has:\n{DEFAULT_WATER} ml of water\n{DEFAULT_MILK} ml of milk\n'
          f'{DEFAULT_BEANS} g of coffee beans\n{DEFAULT_DISPOSABLE_CUPS} disposable cups\n${DEFAULT_COST} of money\n')


def ask_for_action() -> str:

    return input('Write action (buy, fill, take):').strip()


def ask_for_coffee_type() -> str:

    return input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:').strip()


def perform_actions(_action: str) -> None:
    if _action == 'buy':

        perform_action_buy()

    if _action == 'fill':

        perform_action_fill()

    if _action == 'take':

        perform_action_take()


def perform_action_buy() -> None:
    coffee_type = int(ask_for_coffee_type())
    water, milk, beans, disposable_cups, money_left = count_new_coffee_machine_data_buy(coffee_type)

    print(f'\nThe coffee machine has:\n{water} ml of water\n{milk} ml of milk\n'
          f'{beans} g of coffee beans\n{disposable_cups} disposable cups\n${money_left} of money')


def count_new_coffee_machine_data_buy(_coffee_type: int) -> list:
    if _coffee_type == 1:
        _water = DEFAULT_WATER - ESPRESSO_WATER
        _milk = DEFAULT_MILK - ESPRESSO_MILK
        _beans = DEFAULT_BEANS - ESPRESSO_BEANS
        _disposable_cups = DEFAULT_DISPOSABLE_CUPS - 1
        _money_left = DEFAULT_COST + ESPRESSO_COSTS

        return [_water, _milk, _beans, _disposable_cups, _money_left]

    if _coffee_type == 2:
        _water = DEFAULT_WATER - LATTE_WATER
        _milk = DEFAULT_MILK - LATTE_MILK
        _beans = DEFAULT_BEANS - LATTE_BEANS
        _disposable_cups = DEFAULT_DISPOSABLE_CUPS - 1
        _money_left = DEFAULT_COST + LATTE_COSTS

        return [_water, _milk, _beans, _disposable_cups, _money_left]

    if _coffee_type == 3:
        _water = DEFAULT_WATER - CAPPUCCINO_WATER
        _milk = DEFAULT_MILK - CAPPUCCINO_MILK
        _beans = DEFAULT_BEANS - CAPPUCCINO_BEANS
        _disposable_cups = DEFAULT_DISPOSABLE_CUPS - 1
        _money_left = DEFAULT_COST + CAPPUCCINO_COSTS

        return [_water, _milk, _beans, _disposable_cups, _money_left]


def perform_action_fill() -> None:
    water_to_add = int(input('Write how many ml of water you want to add:'))
    milk_to_add = int(input('Write how many ml of milk you want to add:'))
    beans_to_add = int(input('Write how many grams of coffee beans you want to add:'))
    disposable_cups_to_add = int(input('Write how many disposable cups you want to add:'))
    water, milk, beans, disposable_cups = count_new_coffee_machine_data_fill(water_to_add, milk_to_add, beans_to_add, disposable_cups_to_add)

    print(f'\nThe coffee machine has:\n{water} ml of water\n{milk} ml of milk\n'
          f'{beans} g of coffee beans\n{disposable_cups} disposable cups\n${DEFAULT_COST} of money')


def count_new_coffee_machine_data_fill(_water_to_add: int, _milk_to_add: int, _beans_to_add: int, _disposable_cups_to_add: int) -> list:
    _water_to_add += DEFAULT_WATER
    _milk_to_add += DEFAULT_MILK
    _beans_to_add += DEFAULT_BEANS
    _disposable_cups_to_add += DEFAULT_DISPOSABLE_CUPS

    return [_water_to_add, _milk_to_add, _beans_to_add, _disposable_cups_to_add]


def perform_action_take() -> None:
    print(f'I gave you ${DEFAULT_COST}')
    money_to_give = count_new_coffee_machine_data_take()

    print(f'\nThe coffee machine has:\n{DEFAULT_WATER} ml of water\n{DEFAULT_MILK} ml of milk\n'
          f'{DEFAULT_BEANS} g of coffee beans\n{DEFAULT_DISPOSABLE_CUPS} disposable cups\n${money_to_give} of money')


def count_new_coffee_machine_data_take() -> int:

    return DEFAULT_COST - DEFAULT_COST


print_coffee_machine_data()
action = ask_for_action()
perform_actions(action), '\n'
