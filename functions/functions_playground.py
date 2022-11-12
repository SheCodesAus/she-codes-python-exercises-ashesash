data = [1 , 4, 2, 66, 5, 3, 32]
min_number = None
for i in data:
    if min_number is None or i <= min_number:
        min_number = i
        print(i)