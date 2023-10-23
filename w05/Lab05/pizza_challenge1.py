import random

def print_pizza_order(pizza):
    print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust with", pizza['toppings'], "on it.")


size = input('Which size do you want for your pizza? ')
crust = input('Which crust do you want for your pizza? ')
toppings = input('Which toppings do you want for your pizza? ')
customer = {'size': size, 'crust': crust, 'toppings': toppings }

print_pizza_order(customer)

