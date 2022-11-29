names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# names = [
#     "Miranda", "Sophie", "Emily", "Taylor", "Anne",
#     "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
#     "Abby", "Sarah", "Teagen", "Abby", "Abby",
#     "Maddie", "Miranda", "Rosie"
# ]

unique = list()
name_count = {}

# for name in names:
#     if name not in unique:
#         unique.append(name)
#         name_count = names.count(name)
#     print(f"{unique} : {name_count}")

for name in range(len(names)):
    name_count[names[name]] = names.count(names[name])

print(name_count)