# tax and tips in a meal
# 219
from random import randint

def solveTax():

    list_tax = [randint(34,55), randint(5,21), randint(1,3)]
    list_log = ['solveTax()', list_tax]
    meal_cost = list_tax[0]
    tip_percent = list_tax[1]
    tax_percent = list_tax[2]

    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total_cost = meal_cost + tip + tax

    list_ans = [tip, tax, round(total_cost)]
    list_log.append(list_ans)

    print('Meal cost: ' + str(meal_cost))
    print('Tip: ' + str(tip))
    print('Tax: ' + str(tax))
    print('Total cost: ' + str(total_cost))

    return list_log

