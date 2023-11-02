#Variables and Data types

'''
Variables are like container that holds data for example we store suger in cantainer
'''
#example:

a= 3 # a is variable and 3 is assign value

print(a)

#output = 3

'''
data types : this tells us the type of value variable holds, this will also help us to do various operations without causing error
'''
#example :

b= 3
print(type(b))
#output : <class 'int'>

##Numeric data : int, float, complex

e = (int(3))
d = (float(3.383))
c= (complex(b))

print( e, d, c)

#output : 3 3.383 (3+0j)



## Text data : str
#exaple :

f= (str("hello"))

print(f)
#output : hello

#Sequence data types : list, tuples

'''
list : this is mutable type and it is an ordered collection of data with elements separeted by comma and enclosed within square
tuple : it is ordered collection of data with elements separated by comma an enclosed within parenthese,tuples are immutable 
'''
#example:

list1 = [3, 4, 5, ["helooo"], [3.442]]
tuple1 = ((2, 3, 4), ("byeeee"), (5.330))

print(f"{list1}\n{tuple1}")

# output : [3, 4, 5, ['helooo'], [3.442]]
# ((2, 3, 4), 'byeeee', 5.33)

## Mapped data: dict, used to store data as dictionary(dict)

dict1= {"name" : "atharva", "age": 20, "canVote": True}

print(dict1)

#output : {'name': 'atharva', 'age': 20, 'canVote': True}
