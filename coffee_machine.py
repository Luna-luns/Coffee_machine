import math

WATER = 200
MILK = 50
BEANS = 15


def ask_for_amount_of_coffee() -> str:

    return input('Write how many cups of coffee you will need:').strip()


def count_needed_ingredients(_amount_of_coffee: int) -> list:
    water = WATER * _amount_of_coffee
    milk = MILK * _amount_of_coffee
    beans = BEANS * _amount_of_coffee
    _ingredients = [water, milk, beans]

    return _ingredients


def show_needed_ingredients(_amount_of_coffee: int, _ingredients: list) -> None:
    if _amount_of_coffee == 1:

        print(f'For {_amount_of_coffee} cup of coffee you will need:\n{_ingredients[0]} ml of water\n{_ingredients[1]} ml of milk\n{_ingredients[2]} g of coffee beans')

    else:

        print(f'For {_amount_of_coffee} cups of coffee you will need:\n{_ingredients[0]} ml of water\n{_ingredients[1]} ml of milk\n{_ingredients[2]} g of coffee beans')


def ask_for_amount_of_water() -> str:

    return input('Write how many ml of water the coffee machine has:').strip()


def ask_for_amount_of_milk() -> str:

    return input('Write how many ml of milk the coffee machine has:').strip()


def ask_for_amount_of_beans() -> str:

    return input('Write how many grams of coffee beans the coffee machine has:').strip()


def ask_for_coffee_suppliers() -> list:
    water_availability = int(ask_for_amount_of_water())
    milk_availability = int(ask_for_amount_of_milk())
    beans_availability = int(ask_for_amount_of_beans())
    _suppliers_availability = [water_availability, milk_availability, beans_availability]

    return _suppliers_availability


def count_cups(_suppliers_availability: list) -> int:
    water = math.floor(_suppliers_availability[0] / WATER)
    milk = math.floor(_suppliers_availability[1] / MILK)
    beans = math.floor(_suppliers_availability[2] / BEANS)
    _cups = min(water, milk, beans)

    return _cups


def extra_cups(_suppliers_availability: list, _amount_of_coffee: int) -> int:
    water = math.floor(_suppliers_availability[0] / WATER) - _amount_of_coffee
    milk = math.floor(_suppliers_availability[1] / MILK) - _amount_of_coffee
    beans = math.floor(_suppliers_availability[2] / BEANS) - _amount_of_coffee
    _extra_cups = min(water, milk, beans)

    return _extra_cups


def print_enough_suppliers_for_coffee(_ingredients: list, _suppliers_availability: list, _cups: int, _amount_of_coffee: int) -> None:
    if (_suppliers_availability[0] != WATER or _suppliers_availability[1] != MILK or _suppliers_availability[2] != BEANS) and\
            ((_suppliers_availability[0] >= _ingredients[0] and _suppliers_availability[0] < WATER * 2) or
             (_suppliers_availability[1] >= _ingredients[1] and _suppliers_availability[1] < MILK * 2) or
             (_suppliers_availability[2] >= _ingredients[2] and _suppliers_availability[2] < BEANS * 2)):

        print('Yes, I can make that amount of coffee')

    elif (_cups >= _amount_of_coffee) and (_suppliers_availability[0] >= WATER * 2 or _suppliers_availability[1] >= MILK * 2 or
                                           _suppliers_availability[2] >= BEANS * 2):
        _extra_cups = extra_cups(_suppliers_availability, _amount_of_coffee)

        print(f'Yes, I can make that amount of coffee (and even {_extra_cups} more than that)')

    elif _suppliers_availability[0] < _ingredients[0] or _suppliers_availability[1] < _ingredients[1] or\
            _suppliers_availability[2] < _ingredients[2]:

        print(f'No, I can make only {_cups} cups of coffee')


suppliers_availability = ask_for_coffee_suppliers()
amount_of_coffee = int(ask_for_amount_of_coffee())
ingredients = count_needed_ingredients(amount_of_coffee)
cups = count_cups(suppliers_availability)
print_enough_suppliers_for_coffee(ingredients, suppliers_availability, cups, amount_of_coffee)
#  show_needed_ingredients(amount_of_coffee, ingredients)
