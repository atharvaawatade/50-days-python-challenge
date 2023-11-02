#Type Casting

'''
Conversio of one data type into other is known as type casting

two types of type casting :

Explicit Conversion : the conversion done by programer manually as per requirement 
Implicit Conversion : the conversion done by python automatically, and python onlyconverts lower to higer types to prevent data loss.

'''

#Example Explicit Conversion :

a = "3"
b = "4"

print(int(a) + int(b))
#output: 7

#Example Implicit Conversion :

c = 3.6
d = 2

print(c+d)
# output : 5.6

'''
Input function : in python we can take user input directly just by using input ().
'''

#example :

f = input("what is your mother's age : ")
e = input("What is your age ")


print(" difference between age : ", int(f) - int(e))

# output : 20