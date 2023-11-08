# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)

def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)

def calculation(a, b):
    addition = a + b
    subtraction = a - b
    # return multiple values separated by comma
    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)

# function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")
