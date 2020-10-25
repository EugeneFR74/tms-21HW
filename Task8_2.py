

def is_polindrome():
    a = str(input("Give a word"))
    for i in range(len(a)//2):
         if a[i] != a[-i -1]:
             return False
         else:
             return True

print( is_polindrome())

