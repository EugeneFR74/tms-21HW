X = float(input("Enter your X number"))
Y = float(input ("Enter your Y number"))


signs = [(X+Y), (X-Y),(X/Y),(X*Y) or "0"]
index = 0

while True:
     choice =input(signs[index])
     if choice == "0":
          break
     index = (index+1) % 4
