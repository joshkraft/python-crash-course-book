def make_pizza(size, *toppings):
    """Summarize the pizza to be baked"""
    print('Making a ' + size + ' pizza with the following toppings: ')
    for topping in toppings:
        print("  - " + topping)