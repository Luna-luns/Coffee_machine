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
water = 400
milk = 540
beans = 120
disposable_cups = 9
money_left = 550


def print_coffee_machine_data() -> None:

    global water, milk, beans, disposable_cups, money_left

    print(f'\nThe coffee machine has:\n{water} ml of water\n{milk} ml of milk\n'
          f'{beans} g of coffee beans\n{disposable_cups} disposable cups\n${money_left} of money\n')


def ask_for_action() -> str:

    return input('Write action (buy, fill, take, remaining, exit):' + '\n').strip()


def ask_for_coffee_type() -> str:

    return input('\n' + 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:' + '\n').strip()


def perform_actions(_action: str) -> None:

    if _action == 'buy':

        perform_action_buy()

    if _action == 'fill':

        perform_action_fill()

    if _action == 'take':

        perform_action_take()

    if _action == 'remaining':

        print_coffee_machine_data()

    if _action == 'exit':

        exit()


def perform_action_buy() -> None:

    coffee_type = ask_for_coffee_type()

    if coffee_type == 'back':

        return

    else:

        _water, _milk, _beans, _disposable_cups, _money_left = sort_coffee_machine_data_buy(coffee_type)

        if _water >= 0 and _milk >= 0 and _beans >= 0 and _disposable_cups >= 0:

            global water, milk, beans, disposable_cups, money_left

            water, milk, beans, disposable_cups, money_left = _water, _milk, _beans, _disposable_cups, _money_left
            print('I have enough resources, making you a coffee!' + '\n')

        elif _water < 0 <= _milk and _beans >= 0 and _disposable_cups >= 0:

            print('Sorry, not enough water!' + '\n')

        elif _water >= 0 > _milk and _beans >= 0 and _disposable_cups >= 0:

            print('Sorry, not enough milk!' + '\n')

        elif _water >= 0 > _beans and _milk >= 0 and _disposable_cups >= 0:

            print('Sorry, not enough beans!' + '\n')

        elif _water >= 0 and _milk >= 0 and _disposable_cups < 0 <= _beans:

            print('Sorry, not enough disposable_cups!' + '\n')


def count_new_coffee_machine_data_buy(constant_water: int, constant_milk: int, constant_beans: int, constant_disposable_cups: int, constant_money_left: int, constant_costs: int) -> list:

    _water = water - constant_water
    _milk = milk - constant_milk
    _beans = beans - constant_beans
    _disposable_cups = constant_disposable_cups - 1
    _money_left = constant_money_left + constant_costs

    return [_water, _milk, _beans, _disposable_cups, _money_left]


def sort_coffee_machine_data_buy(_coffee_type: str) -> list:

    if _coffee_type == '1':

        return count_new_coffee_machine_data_buy(ESPRESSO_WATER, ESPRESSO_MILK, ESPRESSO_BEANS, disposable_cups, money_left, ESPRESSO_COSTS)

    if _coffee_type == '2':

        return count_new_coffee_machine_data_buy(LATTE_WATER, LATTE_MILK, LATTE_BEANS, disposable_cups, money_left, LATTE_COSTS)

    if _coffee_type == '3':

        return count_new_coffee_machine_data_buy(CAPPUCCINO_WATER, CAPPUCCINO_MILK, CAPPUCCINO_BEANS, disposable_cups, money_left, CAPPUCCINO_COSTS)


def perform_action_fill() -> None:

    water_to_add = int(input('\n' + 'Write how many ml of water you want to add:' + '\n'))
    milk_to_add = int(input('Write how many ml of milk you want to add:' + '\n'))
    beans_to_add = int(input('Write how many grams of coffee beans you want to add:' + '\n'))
    disposable_cups_to_add = int(input('Write how many disposable cups you want to add:' + '\n'))
    count_new_coffee_machine_data_fill(water_to_add, milk_to_add, beans_to_add, disposable_cups_to_add)


def count_new_coffee_machine_data_fill(_water_to_add: int, _milk_to_add: int, _beans_to_add: int, _disposable_cups_to_add: int) -> None:

    global water, milk, beans, disposable_cups

    water += _water_to_add
    milk += _milk_to_add
    beans += _beans_to_add
    disposable_cups += _disposable_cups_to_add


def perform_action_take() -> None:

    print(f'\nI gave you ${money_left}\n')
    count_new_coffee_machine_data_take(money_left)


def count_new_coffee_machine_data_take(_money_left: int) -> None:

    global money_left

    money_left -= _money_left


while True:
    action = ask_for_action()
    perform_actions(action)
