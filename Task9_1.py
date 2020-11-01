list_of_strings =[ "Great job Carl", "It has been a hard day", "Opportunity rises"]



new_list = ["{} -> {}".format(i, el) for i,el in enumerate(list_of_strings)]

print( new_list)