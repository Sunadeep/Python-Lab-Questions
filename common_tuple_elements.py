first_tuple = (1, 2, 3, 4)
second_tuple = (3, 4, 5, 6)

common_elements = []

for number in first_tuple:
    if number in second_tuple:
        common_elements.append(number)

print("Common elements:", tuple(common_elements))
