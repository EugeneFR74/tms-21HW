def fact2(n):

    if n <= 0:
        return 1
    else:
        return n * fact2(n-2)

print(fact2(7))
