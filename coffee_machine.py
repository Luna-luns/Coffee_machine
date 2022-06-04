def ask_for_amount_of_coffee() -> str:
    return input('Write how many cups of coffee you will need:').strip()


def count_needed_ingredients(_amount_of_coffee: int, water=200, milk=50, beans=15) -> str:
    water *= _amount_of_coffee
    milk *= _amount_of_coffee
    beans *= _amount_of_coffee
    if _amount_of_coffee == 1:
        return f'For {_amount_of_coffee} cup of coffee you will need:\n{water} ml of water\n{milk} ml of milk\n{beans} g of coffee beans'

    return f'For {_amount_of_coffee} cups of coffee you will need:\n{water} ml of water\n{milk} ml of milk\n{beans} g of coffee beans'


amount_of_coffee = int(ask_for_amount_of_coffee())
print(count_needed_ingredients(amount_of_coffee))
