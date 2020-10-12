quantity = int(input("Enter the number of possible guests!"))

if quantity > 50:
    print("restaurant!")
if quantity > 20 and quantity < 50:
        print("coffee!")
else:
    print("home!")
