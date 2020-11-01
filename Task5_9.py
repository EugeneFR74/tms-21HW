m = int(input())
n = int(input())

x = range(m,n +1)

for i in x:
    for el in range(2,i-1):
        if i % el ==0:
            print("Number:", i, "Divder:",el)

