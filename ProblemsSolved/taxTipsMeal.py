#tax and tips in a meal

meal_cost = 12
tip_percent = 8
tax_percent = 20

def solve(meal_cost, tip_percent, tax_percent):

    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    total_cost = meal_cost + tip + tax

    print(int(round(total_cost)))
    return int(round(total_cost))

print(solve(meal_cost,tip_percent,tax_percent))