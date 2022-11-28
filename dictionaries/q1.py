import pprint

### DICTIONARIES
# dictionaries are mappings of key-value pairs
# syntax:
# my_dict = {
#     'key1': 'value1',
#     'key2' : 'value2'
# }

prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}

# print(list(i for i in prices)) 
# for i in prices:
#     prices_items = prices[i]
#     print(f"{i}: ${prices_items}")
# print("\n")

# for item, price in prices.items():
#     # print(f"{item}: ${price}")
#     goods_prices = price

# for item, quantities in quantity.items():
#     goods_quantity = quantities

# for items in prices.keys():
#     print(f"{quantities} {items} @ ${price} = {price * quantities}")


#dictionary comprehension
# result = {key: round(prices[key] * quantity[key],2) for key in prices}
# pprint.pprint(f"{result}")

#method2
for key in prices:
    result = round(prices[key]*quantity[key],2)
    print(f"{quantity[key]} {key} @ ${prices[key]} = ${result}")
