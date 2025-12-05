# Write your code here.

# Task 1

def hello():
    return 'Hello!'
print(hello())

# Task 2

def greet(name):
    return f'Hello, {name}!'
# print(greet('Jessica'))

# Task 3 Calculator

def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
# print(calculator(2,3))

# Task 4 data type
  
def data_type_conversion(value, dtype):
    try:
        if dtype == "float":
            return float(value)
        elif dtype == "int":
            return int(value)
        elif dtype == "str":
            return str(value)
        else:
            return "Unknown data type"
    except ValueError:
        return f"You can't convert {value} into a {dtype}."


# task 5 average

def grade (*args):
    try:
        grade_avg = (sum(args)) / (len(args))
    # print(sum(args))
    # print(type())
        if grade_avg >= 90:
           return 'A'
        elif grade_avg >79 and grade_avg <90:
           return 'B'
        elif grade_avg >69 and grade_avg <80:
            return 'C'
        elif grade_avg >59 and grade_avg <70:
           return  'D'
        else:
            return 'F'
    # except ValueError:
        # return f'Invalid data was provided.'
    except TypeError:
        return f'Invalid data was provided.'
print(grade(75,85,95))
