my_list = [2, 6, 7, 9]
i = 0
for element in my_list:
    my_list[i] = element * (-2)
    i += 1
print(my_list)

my_list = [2, 6, 7, 9]

i = 0

while i < len(my_list):
    print(my_list[i] * (-2), end="")
    i += 1



