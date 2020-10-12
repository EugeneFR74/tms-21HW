def cm_to_inches():
    cm = float(input("Choose your value for conversion process!:"))
    inches = cm * 0.393
    print(cm, " centimeters", "are equal to", inches, "inches")
    return inches


print(cm_to_inches())


def inches_to_cm():
    inch_value = float(input("Choose your value for conversion process!:"))
    cm = inch_value / 0.393
    print(inch_value, "inches", "are equal to", cm, "centimeters")
    return cm


print(inches_to_cm())


def miles_to_km():
    miles = float(input("Enter your value"))
    km = miles / 0.62
    print(miles, "miles are equal to", km, "kilometers")
    return km


print(miles_to_km())


def km_to_miles():
    km = float(input("Enter you value"))
    miles = km * 0.62
    print(km, "kilometers equal", miles, "miles")
    return miles


print(km_to_miles())


def pounds_to_kg():
    pounds = float(input("Give you values"))
    kg = pounds / 2.20
    print(pounds, "pounds are equal to", kg, "kg")
    return kg


print(pounds_to_kg())


def kg_to_pounds():
    kg = float(input("Give your suited conversion"))
    pounds = kg * 2.20
    print(kg, "kilograms are equal to", pounds, "pounds")
    return pounds


print(kg_to_pounds())


def ounces_to_grams():
    ounce = float(input("Enter your value"))
    gram = ounce / 0.035
    print(ounce, "ounces are equal to", gram, "grams")
    return gram


print(ounces_to_grams())


def grams_to_ounces():
    gram = float(input("Enter your value"))
    ounce = gram * 0.035
    print(gram, "grams are equal to", ounce, "ounces")
    return ounce


print(grams_to_ounces())


def gallons_to_litres():
    gallon = float(input("Give your value"))
    litre = gallon / 0.264
    print(gallon, "gallons are standing for", litre, "litres")
    return litre


print(gallons_to_litres())


def litres_to_gallons():
    litre = float(input("Give your value"))
    gallon = litre / 0.264
    print(litre, "litres are standing for", gallon, "gallons")
    return gallon

print(litres_to_gallons())


def pints_to_litres():
    pint = int(input("Give your value"))
    litre = pint / 2.127
    print(pint, "pints are same as ", litre, "litres")
    return litre


print(pints_to_litres())


def litres_to_pints():
    litre = int(input("Give your value"))
    pint = litre * 2.127
    print(litre, "litres are same as ", pint, "pints")
    return pint


print(litres_to_pints())
