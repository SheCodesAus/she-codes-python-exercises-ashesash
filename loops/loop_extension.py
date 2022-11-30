# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]

# for items in groceries:

#     quantity = int(input("how many would you like?"))

#q2
rows = int(input("Enter number of rows: "))

# for i in range(rows):
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")
# print(range(rows))

#q3

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  @")