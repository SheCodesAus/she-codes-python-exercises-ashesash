import csv

#q1
# with open ("colours_20_simple.csv") as colours_csv:
#     reader = csv.reader(colours_csv)
#     # next(colours_csv)
#     for row in reader:
#         print(row[2])

#q2
# with open("colours_20_simple.csv") as colours_csv:
#     colours_csv_reader = csv.reader(colours_csv)
#     header = next(colours_csv_reader)
    # for row in colours_csv_reader:
    #     print(f"{row[2]}, Hex: {row[1]}, RGB: {row[0]}")

#     casted_colours_list = list(colours_csv_reader)
#     print(casted_colours_list)

#     for row in colours_csv_reader:
#         print(f"{row[2]}, Hex: {row[1]}, RGB: {row[0]}")
#         colours_list.append(row)

#question 4
#red, green, blue, yellow
# counters = [0,0,0,0]

# with open("colours_20.csv") as colours_csv:
#     reader = csv.reader(colours_csv)
#     for row in reader:
#         if "red" in row[4]:
#             red_counter += 1
        

#q5
# min_veloctiy = 99999999
# max_velocity = 0

# with open("galaxies.csv") as galaxies_csv:
#     reader = csv.reader(galaxies_csv)
#     next(galaxies_csv)
#     for rwo in reader:
#         if int(row[1]) > max_velocity:
#             max_velocity = int(row[1])
#             max_galxy = row[0]
#             print(f"updated  value of {max_velocity}")
            
#q3
# with open("colours_20.csv", 'r') as colours_csv:
#     reader = csv.reader(colours_csv)
#     header = next(reader)
#     for row in reader: 
#         print(f"{row[4]}, Hex: {row[2]}, RGB: {row[1]}")
