my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
new_dict = {}
dict_key = list(my_dict.keys())

for key in dict_key:
    length = len(dict_key)
    new_key = key + str(length)
    new_dict[new_key] = my_dict[key]

print(new_dict)


new_dict1 = {}

dict_key = list(my_dict.keys())

i = 0
while i < len(dict_key):
    new_dict1 = dict_key[i]+ str(len(dict_key))


print(new_dict1)