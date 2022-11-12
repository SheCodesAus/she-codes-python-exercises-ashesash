my_dict = {
    'baby Spinach': 2.78,
    'hot chocolate': 3.70,
    'crackers': 2.10,
    'Bacon': 9.00,
    'Carrots': 0.56,
    'Oranges': 3.08 
}

# print(my_dict['Bacon'])

# add a new item
my_dict['Avocados'] = 1.00

#change existing item
my_dict['hot chocolate'] = 2.70

#removing an item
del my_dict['baby Spinach']

# iterate in a dictionary
for item in my_dict:
    value_item = my_dict[item]
    print(f"{item}: {value_item}")

#method 2
for item in my_dict.keys():
    print(item)
for item in my_dict.values():
    print(item)

#method 3
#tuple unpacking
for item,price in my_dict.items(): 
    print(f"{item}: ${price}")
