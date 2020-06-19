
# Given names of a few people ["Ben", "Devika", "Shivani", "Stuti"]. Do
# the following 4 questions. Feel free to invent values for the dictionary.
#
# 1. For the above mentioned names of people write a dictionary that
# stores the cellphone number of the people by name
#
# 2. For the above mentioned names of people write a dictionary that
# stores the age of the people by name
#
# 3. For the above mentioned names of people write a dictionary that
# stores the address of the people by name
#
#
# 4. Then write a loop, you are free to use for or while, to print
# age, address, and cellphone numbers.

#For the above mentioned names of people write a dictionary that
# stores the cellphone number of the people by name

cellphone_no = {}
cellphone_no["Ben"] = "987231450"
cellphone_no["Devika"] = "9318393776"
cellphone_no["Stuti"] = "8927291234"
cellphone_no["Shivani"] = "98735392911"

print(len(cellphone_no))

list_of_keys =cellphone_no.keys()

counter=0
print(list_of_keys)
while counter < len(list_of_keys):
    key=list_of_keys[counter]
    value=cellphone_no[key]
    print("for the name {} the cellphone no is {}".format(key,value))
    counter=counter + 1

#For the above mentioned names of people write a dictionary that
# stores the age of the people by name

dictonary_for_age ={}
dictonary_for_age["Ben"] = "35"
dictonary_for_age["Devika"] = "23"
dictonary_for_age["Stuti"] = "30"
dictonary_for_age["Shivani"] = "33"


print(len(dictonary_for_age))

list_of_keys = dictonary_for_ag

counter=0

while counter < len(list_of_keys):
    key=list_of_keys[counter]
    value=dictonary_for_age[key]
    print("for the name {} the age of this person is {}".format(key,value))
    counter=counter + 1

#For the above mentioned names of people write a dictionary that
# stores the address of the people by name


dictonary_for_address ={}
dictonary_for_address["Ben"] = "03,club drive,NY"
dictonary_for_address["Devika"] = "10,newton lane,New delhi"
dictonary_for_address["Shivani"] = "123,costal apartment,Mumbai"
dictonary_for_address["Stuti"] = "556,lincasta apartment,New Delhi"


print(len(dictonary_for_address))

list_of_keys = dictonary_for_address

counter=0

while counter < len(list_of_keys):
    key=list_of_keys[counter]
    value=dictonary_for_address[key]
    print("for the name {} the address of this person is {}".format(key,value))
    counter=counter + 1

 #Then write a loop, you are free to use for or while, to print
# age, address, and cellphone numbers.


list_of_keys = [cellphone_no ,dictonary_for_address ,dictonary_for_age]

counter=0

while counter < len(list_of_keys):
    key=list_of_keys[counter]
    value=[dictonary_for_address,cellphone_no,dictonary_for_age][key]
    print("for the name {} the details of this person is {}".format(key,value))
    counter=counter + 1