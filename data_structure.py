# 1. Tuples
cars = ("Mercedes", "R34", "Pagani", "Supra", "GTR")
print(cars)
print(cars[2])
print(cars[1:4])
print(cars[1:])
for gari in cars:
    print(gari)

# 2. lists
colours = ["Red", "Green", "Purple", "Blue", "Grey", "Black"]
print(colours)
print(colours[2])
colours[0] = "Light Red"
print(colours[1:4])
print(colours[1:])
for rangi in colours:
    print(rangi)
colours.reverse()
print(colours)
colours.pop(1)
print(colours)
colours.sort(reverse=True)
print(colours)

# 3.Dictionaries
students = {"ADM1": "Tracy", "ADM2": "Moses", "ADM3": "Eugene"}
print(students["ADM1"])
for funguo in students.keys():
    print(funguo)

for jina in students.values():
    print(jina)

# 4.Sets

# assignment
def filter_list (input_list):
    new_list = []
    for item in input_list:
        if len(item) > 5:
            new_list.append(item)
    return new_list
my_list = ["apple", "Samsung", "Huwawei", "Tecno", "Nokia", "Telefunken"]
filtered_list = filter_list(my_list)
print(filtered_list)



