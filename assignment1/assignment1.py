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
# print(grade(75,85,95))

# Task 6: Use a For Loop with a Range
#
def repeat(str, cnt):
    
    result = ''
    for i in range(cnt):
        result += str
    return result
        
# print(repeat('hi',3))

# Task 7: Student Scores, Using **kwargs

def student_scores(mode, **kwargs):
    if mode == "best":
        best_name = ""
        best_score = 0

        for name, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_name = name

        return best_name

    elif mode == "mean":
        total = 0
        count = 0

        for score in kwargs.values():
            total += score
            count += 1

        return total / count
# Task 8: Titleize, with String and List Operations
# Create a function called titleize. It accepts one parameter, a string. The function returns a new string, where the parameter string is capitalized as if it were a book title.
# The rules for title capitalization are: (1) The first word is always capitalized. (2) The last word is always capitalized. (3) All the other words are capitalized, except little words. For the purposes of this task, the little words are "a", "on", "an", "the", "of", "and", "is", and "in".
# The following string methods may be helpful: split(), join(), and capitalize(). Look 'em up.
# The split() method returns a list. You might store this in the words variable. words[-1] gives the last element in the list.
# The in comparison operator: You have seen in used in loops. But it can also be used for comparisons, for example to check to see if a substring occurs in a string, or a value occurs in a list.
# A new trick: As you loop through the words in the words list, it is helpful to have the index of the word for each iteration. You can access that index using the enumerate() function:
# for i, word in enumerate(words):

def titleize(str):
    little_words = ["a", "on", "an", "the", "of", "and", "is","in"] 
    for i, word in enumerate(str):
        if word in little_words:
            
# Write your code here.git pul
