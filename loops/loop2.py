name_list = ["ash", "bunny", "joy", "kitty"]

# for name in name_list:
#     print(f"hi {name}")
#     input("-----")

#while loop
# counter = 0
# while counter < len(name_list):
#     print(f"hi {name_list[counter]}")
#     print(counter)
# counter+=1

#-----------------------------------------------------
#example 2
import random
budget = 100 #dollars
how_much_spent = 0 # dollars

def buy_stuff():
    cost_of_item = random.randint(0,20)
    return cost_of_item

how_much_spent += buy_stuff()
print(f"total spent: {how_much_spent}")

if how_much_spent < budget:
    how_much_spent += buy_stuff()
    print(f"total spent: {how_much_spent}")

while how_much_spent < budget:
    how_much_spent += buy_stuff()
    print(f"total spent: {how how_much_spent}")

    input("-----")

for i in range(0,100):
    how_much_spent += buy_stuff()
    print(f"total spent: {how_much_spent}")

    input ("---")
    if how_much_spent > budget:
        break