
# Example 1: Basic while loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

# Explanation:
# This is a basic while loop that iterates as long as 'count' is less than 5. 
# It prints the value of 'count' and increments it in each iteration.

# Example 2: Using break statement
num = 0
while True:
    if num >= 5:
        break
    print(f"Number is {num}")
    num += 1

# Output:
# Number is 0
# Number is 1
# Number is 2
# Number is 3
# Number is 4

# Explanation:
# In this example, we use an infinite while loop. The 'break' statement is used to exit the loop when 'num' becomes greater than or equal to 5.

# Example 3: Using continue statement
even_numbers = []
num = 0
while num < 10:
    num += 1
    if num % 2 != 0:
        continue
    even_numbers.append(num)

print("Even numbers:", even_numbers)

# Output:
# Even numbers: [2, 4, 6, 8, 10]

# Explanation:
# This while loop iterates through numbers from 1 to 10. The 'continue' statement is used to skip odd numbers and only append even numbers to the list.

# Example 4: Nested while loops
outer_loop = 1
while outer_loop <= 3:
    inner_loop = 1
    while inner_loop <= 3:
        print(f"Outer: {outer_loop}, Inner: {inner_loop}")
        inner_loop += 1
    outer_loop += 1

# Output:
# Outer: 1, Inner: 1
# Outer: 1, Inner: 2
# Outer: 1, Inner: 3
# Outer: 2, Inner: 1
# Outer: 2, Inner: 2
# Outer: 2, Inner: 3
# Outer: 3, Inner: 1
# Outer: 3, Inner: 2
# Outer: 3, Inner: 3

# Explanation:
# This example demonstrates nested while loops, where an outer loop controls the inner loop's execution.

# Example 5: Using while-else
number = 5
while number > 0:
    print(number)
    number -= 1
else:
    print("Loop finished!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Loop finished!

# Explanation:
# The 'else' block is executed when the while loop completes without being interrupted by a 'break' statement.

# Example 6: Avoiding infinite loops
# Uncomment the following code to see how to avoid infinite loops
# while True:
#     user_input = input("Enter 'q' to quit: ")
#     if user_input == 'q':
#         break

# Explanation:
# Infinite loops can be dangerous, and they are usually avoided. In this example, the user can exit the loop by entering 'q'.

