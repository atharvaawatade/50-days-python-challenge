# String Methods 
#python provides set of built in methods that can use to alter and modify the string

#upper () : converts the string in upper case
#example : 

str1 = "Absjvjsl"
print(str1.upper())
#output : ABSJVJSL

#lower(): converts string into lower case

print(str1.lower())
#output : absjvjsl

#rstrio() : removes the trailing character 

str2 = "helooo !!!!"
print(str2.rstrip("!"))
#output : helooo

#replace() : this method replaces all occurnces of string with another string

print(str2.replace("!!!", "byee"))
#output : helooo byee!

#split() : it splits the given string at the specific instance and returns the separated strings as list items

print(str2.split(" "))
#output : ['helooo', '!!!!']

#Capitalize(): converts first character in upper and others in lower case

str3 = "sHlsdjaGDFDF"
print(str3.capitalize())
#output : Shlsdjagdfdf

#Center() : aligns the string to center by parameters given by user

print(str3.center(20))
#outptu :     sHlsdjaGDFDF

# Count() : this method returns the number of times the given value has occurred within the given string

print(str3.count("s"))
# output : 2

# endswith() : this method checks if the strings ends with given value if yes then returns true else false

print(str3.endswith("FDF"))
#output : True

#in endswith we can alsocheck for a value in-between the string by providing start and end index positions.

print(str3.endswith("G", 3, 8))
#OUTPUT : True

#find() : searches the first occurance of the given value and returns the index where it is present, if given value is absent from the string then it returns -1.

print(str3.find("G"))
#output : 7

# index() : similar to the find but if given value is not present it raise exception

print(str3.index("F"))
#output : 10

#isalnum : this method returns true, only if the entire string only consits of A-Z;a-z;0-9

print(str3.isalnum())
#output : True

#isalpha : this method returns true, if the entire string consists of A-Z; a-z. if other character then it returns false

print(str3.isalpha())
#output : True

#islower : this method returns true if all the characters in the string are lower case else it returns false

print(str3.islower())
#output : False

#isprintable : this method return if all characters within string are printable else return false

print(str3.isprintable())
#output : True

str4 = "helooo \n"
print(str4.isprintable())
#output : False

#isspace : this methode returns true only and only if the string contains white space else return false 

print(str3.isspace())
#output : False

#istitle : true only when all the first letter of string is capital else return false

print(str1.istitle())
#output : True

#startwith(): checks if the string starts with the given value then only returns true else false

print(str3.startswith("s"))
#output : True

#swapcase(): converts lower case to upper case and vice-versa

print(str3.swapcase())
#output : ShLSDJAgdfdf

#title (): It capitalized each letter of the word within the string

print(str3.title())
#output : Shlsdjagdfdf

