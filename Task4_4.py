my_list = ["Great", "Awesome", "Exquisite"]

for word in range(len(my_list)):
    new_list1 = my_list[1:] + my_list[:1]

print(new_list1, end=' ')



my_list = ["Great", "Awesome", "Exquisite"]

index = 0
while index < len(my_list):
     new_list2 = my_list[1:] + my_list[:1]
     index +=1


print (new_list2, end = ' ')
