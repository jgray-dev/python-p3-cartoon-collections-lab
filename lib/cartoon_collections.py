def roll_call_dwarves(dwarfs):
    i = 1
    for dwarf in dwarfs:
        print(f"{i}. {dwarf}")
        i += 1


def summon_captain_planet(planeteer_calls):
    return [f"{each.title()}!" for each in planeteer_calls]


def long_planeteer_calls(planeteer_calls):
    for call in planeteer_calls:
        if len(call) > 4:
            return True
    return False


cheeses = ["camembert", "gouda", "cheddar"]


def find_the_cheese(list):
    for ing in list:
        if ing in cheeses:
            return ing
    return None
