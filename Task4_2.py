list_1 = [1,54,45,78,52,64,90,100]

even_number, odd_number = 0, 0

i = 0

while (i <len(list_1)):
    if list_1[i] % 2 == 0:
        even_number +=1
    else:
        odd_number +=1
    i +=1

print ("The amount of evzn numbers is :", even_number)
print ("The amount of odd number is:" , odd_number)

list_1 = [1,54,45,78,52,64,90,100]
even_number, odd_number =0,0
for nums in list_1:
	if nums % 2 ==0:
		even_number +=1
	else:
		odd_number +=1

print ("evens are :", even_number)
print ("odds are :", odd_number )
