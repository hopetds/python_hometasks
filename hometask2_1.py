#! python
#Hometask2_1 by ILYA_KHAMIAKOU
# setting up key list
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# setting up values list
list2 = [1, 2, 3, 4]
def dic():
    keys=list1 #local list1 variable
    values=list2 #local list2 varialbe
    keys_len = len(keys)  # keys list length
    for i in range(keys_len):
        for j in range(len(values)):
            if keys[i] != values[j]:
                values.append("None")
    values_cut = values[:keys_len]
    dictionary=dict(zip(keys,values_cut)) # making a dictionary
    print(dictionary)
dic()