from fighter import Fighter


def combat(one: Fighter, two: Fighter):
    if not one.isalive():
        print(f'{one.name} is dead. {two} has {two.hp} health.')
        return
    one.strike(two)
    return combat(two, one)