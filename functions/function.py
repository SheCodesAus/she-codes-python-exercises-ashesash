#q1
# def far_to_cel(temp):
#     #temp = input("enter temp")
#     cel = (temp - 32) * 5/9
#     return cel

# print(far_to_cel(float(input("enter temp: "))))

#q4

def price(price_unit, num_units):
    price_total = price_unit * num_units
    return price_total

print(price(float(input("enter price per unit: ")), float(input("enter number of units: "))))