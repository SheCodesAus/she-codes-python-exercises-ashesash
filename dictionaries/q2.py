colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}


colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

#dictionary comprehension
# colour_counts = {x: colours.count(x) for x in colours}
# print(colour_counts)

for colour in colour_counts:
    colour_counts = colours.count(colour)
    print(f" {colour}: {colour_counts}")

# colours = [
#     "orange",
#     "purple",
#     "blue",
#     "yellow",
#     "green",
#     "green",
#     "purple",
#     "purple",
#     "green",
#     "blue",
#     "green",
#     "orange",
#     "purple",
#     "blue",
#     "green",
#     "orange",
#     "orange",
#     "red",
#     "yellow",
#     "yellow"
# ]
