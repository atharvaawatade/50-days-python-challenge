# Example 1: Using a for loop to iterate through a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# Explanation:
# In this example, we have a list of fruits. We use a for loop to iterate through each element (fruit) in the list and print it.

# Example 2: Using range() in a for loop

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Explanation:
# The range() function generates a sequence of numbers from 0 to 4. The for loop iterates through these numbers and prints each one.

# Example 3: Using for loop to iterate through a dictionary

student_grades = {"Alice": 95, "Bob": 88, "Charlie": 92}
for student, grade in student_grades.items():
    print(f"{student} scored {grade} marks")

# Output:
# Alice scored 95 marks
# Bob scored 88 marks
# Charlie scored 92 marks

# Explanation:
# In this example, we have a dictionary containing student names and their grades. The for loop iterates through the dictionary using the items() method and prints each student's name and grade.

# Example 4: Using for loop with else block

numbers = [1, 2, 3, 4, 5]
search_number = 6
for number in numbers:
    if number == search_number:
        print(f"{search_number} found!")
        break
else:
    print(f"{search_number} not found!")

# Output:
# 6 not found!

# Explanation:
# This example demonstrates how to use the else block with a for loop. It searches for a specific number in the list and prints a message if found. If the loop completes without finding the number, it prints a message in the else block.

# Example 5: Using nested for loops

for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")

# Output:
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
# (2, 0)
# (2, 1)

# Explanation:
# Nested for loops are used to generate combinations of values from two ranges. In this example, we iterate through two ranges and print their combinations.
