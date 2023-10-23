import random

def print_pizza_order(pizza):
    print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust")
    print("With", pizza['toppings'], "on it")

monday = {'size': "small", 'crust': "traditional", 'toppings': "extra cheese"}
friday = {'size': "large", 'crust': "deep dish", 'toppings': "pepperoni"}
student = {'size': "large", 'crust': "cheese burst", 'toppings': "sausage"}
pizza_list = [monday, friday, student]
pizza = random.choice(pizza_list)

print_pizza_order(pizza)

