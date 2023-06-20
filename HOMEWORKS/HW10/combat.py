from fighter import Fighter


def combat(one: Fighter, two: Fighter):
    if not one.isalive():
        print(f'{one} is dead')
        return
    one.strike(two)
    return combat(two, one)