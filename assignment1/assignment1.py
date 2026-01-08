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
# Create a function called student_scores. It takes one positional parameter and an arbitrary number of keyword parameters. The positional parameter is either "best" or "mean". If it is "best", the name of the student with the higest score is returned. If it is "mean", the average score is returned.
# As you are using **kwargs, your function can access a variable named kwargs, which is a dict. The next lesson explains about dicts. What you need to know now is the following:
# A dict is a collection of key value pairs.
# You can iterate through the dict as follows:
# for key, value in kwargs.items():
# You can also get kwargs.keys() and kwargs.values().
# The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as the value for each.

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
    result = []
    words = str.split()
    for i, word in enumerate(words):
        
        if i == 0:
            result.append(word.capitalize())
        
        elif i == len(words) - 1:
            result.append(word.capitalize())

        elif word in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())

    return " ".join(result)

# Task 9: Hangman, with more String Operations
# Create a function hangman. It takes two parameters, both strings, the secret and the guess.
# The secret is some word that the caller doesn't know. So the caller guesses various letters, which are the ones in the guess string.
# A string is returned. Each letter in the returned string corresponds to a letter in the secret, except any letters that are not in the guess string are replaced with an underscore. The others are returned in place. Not everyone has played this kid's game, but it's common in the US.
# Example: Suppose the secret is "alphabet" and the guess is "ab". The returned string would be "a___ab__".
# Note that Python strings are immutable. That means that the following code would give an error:
# secret = "alphabet"
# secret[1] = "_"
# On the other hand, you can concatenate strings with the + operator.

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10: Pig Latin, Another String Manipulation Exercise
# Pig Latin is a kid's trick language. Each word is modified according to the following rules. (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. 
# (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
# Create a function called pig_latin. It takes an English string or sentence and converts it to Pig Latin, returning the result. We will assume that there is no punctuation and that everything is lower case.

def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:

        # starts with vowel
        if word[0] in vowels:
            result.append(word + "ay")

        # starts with "qu"
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")

        # has consonant + "qu" (e.g. "square")
        elif word[1:3] == "qu":
            result.append(word[3:] + word[:3] + "ay")

        # normal consonant cluster
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                index += 1

            result.append(word[index:] + word[:index] + "ay")

    return " ".join(result)
