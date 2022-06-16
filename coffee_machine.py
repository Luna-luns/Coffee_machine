from CoffeeMachine import CoffeeMachine


coffee_machine = CoffeeMachine()
while True:
    state = coffee_machine.get_state()
    if state == CoffeeMachine.WAIT_COMMAND:
        print('Write action (buy, fill, take, remaining, exit):')

    if state == CoffeeMachine.WAIT_WATER:
        print('\n' + 'Write how many ml of water you want to add:')

    if state == CoffeeMachine.WAIT_MILK:
        print('Write how many ml of milk you want to add:')

    if state == CoffeeMachine.WAIT_BEANS:
        print('Write how many grams of coffee beans you want to add:')

    if state == CoffeeMachine.WAIT_CUPS:
        print('Write how many disposable cups you want to add:')

    if state == CoffeeMachine.WAIT_COFFEE_TYPE:
        print('\n' + 'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')

    action = input()
    answer = coffee_machine.execute_command(action)
    if answer != '':
        print(answer)
