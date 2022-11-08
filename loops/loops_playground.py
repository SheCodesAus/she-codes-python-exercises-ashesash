# for num in range(101):
#     print(num)

# for num in range(0,101,5):
#     print(num)
    
for _ in range(0,4):
    print('hello')

for letter in "Joy":
    print(letter)

wishlist = ["igloo", "chicken", "donut toy"]

# for item in range(len(wishlist))
#       print(f"chilli wants: {item}")

chilli_wishlist = [
    ["igloo"],
    ["donut toy", "toyotoy"]
]

for category in chilli_wishlist:
    for item in category:
        print(item)

#while loop

counter = 10
while counter <=10:
    print(counter)
    counter += 1

guess = ""
while guess != "a":
    guess = input("guess a letter: ")
    
