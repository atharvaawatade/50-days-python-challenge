#If else condition statement

'''
Sometimes we need to check the evaluation of certain expression, whether the expression  evaluation to true or false if the expression evaluates to false then program execution follow a diffrent path the true value

based on this statement further classsified to :

IF
IF-ELSE
IS-ELSE-ELIF
NEASTED IF-ELSE-IF

----Conditional operators:
>, <, <=, >=, ==, !=
'''

fruitprice1 = float(input("Enter the fruit price: "))
budget1 = 200

if fruitprice1 <= budget1:
    print("Buy this")
else:
    print("Don't buy this")

## elif statemet : sometimes we need to evaluate more than one condition. this can be done using elif statement
print("lets move on to the elif statement \n")

fruitprice2 = float(input("Enter the fruit price: "))
budget2 = 200

if fruitprice2 > budget2 :
    print("Don't Buy this")

elif fruitprice2 <= 100 :
    print("yayy!! you saved 100 rs")

else :
    print("buy this")

 ##Nested statement :- we can use if, if-else, elif statements inside other if statements as well


Number = int(input("Enter registration number between 1 - 400: "))

Number = int(input("Enter registration number between 1 - 400: "))

if Number == 0:
    print("Re-evaluation")
elif Number > 0 and Number <= 100:
    print("Your class is A")
elif Number > 100 and Number <= 200:
    print("Your class is B")
    if Number > 200 and Number <= 300:
        print("Your class is C")
    else:
        print("Result not updated")
else:
    print("You have failed")
