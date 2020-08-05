# tax and tips in a meal
# 219

from random import randint
import aidfunctions

def solveTax():

    list_tax = [randint(34, 55), randint(5, 21), randint(1, 3)]
    meal_cost = list_tax[0]
    tip_percent = list_tax[1]
    tax_percent = list_tax[2]

    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total_cost = meal_cost + tip + tax

    list_ans = [tip, tax, round(total_cost)]

    print('Meal cost: ' + str(meal_cost))
    print('Tip: ' + str(tip))
    print('Tax: ' + str(tax))
    print('Total cost: ' + str(total_cost))

    return aidfunctions.append_elements('solveTax()', list_tax, list_ans)

