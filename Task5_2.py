n = int(input("Enter your number"))
sum = 0
multi = 1

while n> 0:
     remainder = n % 10
     sum = sum + remainder
     multi = multi * remainder
     n= n // 10

print ("Sum equals to", sum)
print ("multi equals to", multi)