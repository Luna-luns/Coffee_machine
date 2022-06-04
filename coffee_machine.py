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

    print(f'For {_amount_of_coffee} cups of coffee you will need:\n{_ingredients[0]} ml of water\n{_ingredients[1]} ml of milk\n{_ingredients[2]} g of coffee beans')


amount_of_coffee = int(ask_for_amount_of_coffee())
ingredients = count_needed_ingredients(amount_of_coffee)
show_needed_ingredients(amount_of_coffee, ingredients)
