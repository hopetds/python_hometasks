#! python
#Hometask2_2 by ILYA_KHAMIAKOU
from functools import reduce
polystring = raw_input("Type smth to find out if it is a palindrome: ") #input
nowhitespace=polystring.replace(" ", "") #removing whitespaces
text=nowhitespace.lower() #whole string is lowercased
punct = ('!',',','?') #define symbols you want to remove
no_punct = reduce(lambda text, p: text.replace(p, ''), punct, text) #removing punct symbols
a = no_punct[::-1] #string reverse
if no_punct == a: #comparing
  print("It is!")
else:
  print("Noooo")
####################
  TESTSTRING: Sa!tor Arep,o! teNet? ,,opEra roTas!!!!
####################