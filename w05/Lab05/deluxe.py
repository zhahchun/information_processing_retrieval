import pprint
address = {
    'street': "1278 Badger Dr",
	'city': "Madison",
	'state': "Wisconsin",
	'zip': 53706
    }

deluxe_pizza = {
   'crust': "thin",
   'size': "extra large",
   'toppings': ["pepperoni",
                "black olives",
                "green peppers",
                "sausage",
                "mushrooms"
               ],
   'address' : address
    }

def print_pizza_order(pizza):
   print("I would like a", pizza['size'], "pizza on a", pizza['crust'], "crust")
   #  print("With ", len(pizza['toppings']), " toppings on it:")
   print("With ", pizza['toppings'][0], " toppings on it")
   print('Send to ' + pizza['address']['street'] + '.' )


# print_pizza_order(deluxe_pizza)
# for i in range(len(deluxe_pizza['toppings'])):
#     print('- ', deluxe_pizza['toppings'][i])
pprint.pprint(deluxe_pizza)


