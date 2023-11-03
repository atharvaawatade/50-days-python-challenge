# String

'''
Anything that enclose between single or double marks is consider as string
it is used when working with unicode 
'''
# example 

name = input('Enter your name: ')

print ("hello " + name)

#output : hello atharva

# we can use double quotes in single quotes vice-versa

print ("hello, 'how are you'")
#output : 'how are you'


#Multi String : we can use ''' ''' for adding multi strings
#example:

a =''' hello
how 
are
you?
'''
print(a)
#output :  hello
# how
# are
# you?

## Accesing characters of string
'''
in python string is like an array of characters we can access parts of string by using its index which start from 0
[] used to access the elements of string
'''
#example :

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#out put : a
# t
# h
# a
# r
# v

# we can loop string using for loop

# example :
print("now for the for loop: \n")
for character in name:
    print(character)
    
    #output : now for the for loop :
# a
# t
# h
# a
# r
# v
# a

### Strings and operations on string

#length of the string : len() function
#example :

fruit = input("Enter fruit name : ")

len = len(fruit)
print ("lengeth of string is: ", len)

#output : for mango : 5

## slicing the string :

# Example:

print ( "now lets move on the slicing:  \n")

print(fruit[0:3])
print(fruit[:4])
print(fruit[2:4])

#output : man
# mang
# ng


# -ve slicing example:

print(fruit[-2:-4])
#output : ng

