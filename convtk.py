
'''
Welcome to the convtk, or "Convenience Toolkit". This is a project of mine meant to take away all of the stacked code and let you
code faster and more readable.
Main Contributor: Fastpast93
'''

#String Tools

def mul_replace(string, dict): # <-- Takes a Replacement Dictionary and a string and replaces any amount of keywords with their respective replacement
    for key, value in dict.items():
        string = string.replace(key, value)
    return string

def string_to_collection(string): #<-- Takes a string and returns a list of each character
    output = []
    for char in string:
        output.append(char)
    return output

#List or Tuple Tools

def collection_to_string(collection): # <-- Takes a List or Tuple and returns a readable string
    output = ""
    for item in collection:
        output += (f"{item}, ")
    return output.removesuffix(", ")

def mul_capitalize(collection): # <-- Takes a List or Tuple and returns the capitalization of the first letter of each string
    output = []
    for string in collection:
        output.append(string.capitalize())
    return output

def mul_case(collection, set_case="upper"): # <--Takes a List or Tuple and sets the case to set_case, default set to uppercase
    output = []
    for string in collection:
        if set_case.lower() == "upper":
            output.append(string.upper)
        elif set_case.lower() == "lower":
            output.append(string.lower())
        return output

def mul_title(collection): # <--Takes a List or Tuple and returns the collection with all of the words capitalized.
    output = []
    for string in collection:
        output.append(string.title())
    return output 


#Dict Tools

def key_value_separator(dict): # <-- Takes a Dict and returns a 2D list of keys and values.
    keys, values = [], []
    for key, value in dict:
        keys, values = keys.append(key), values.append(value)
    return [keys, values]
    
#Math Tools

def sqrt(num): # <-- Takes a number and returns its square root
    return num ** 0.5

def sqre(num): # <-- Takes a number and returns the square
    return num ** 2

def calculate_hypotenuse(leg_a, leg_b): # <-- takes leg a and leg b of a right triangle and returns the hypotenuse
    return sqrt(sqre(leg_a)) + (sqre(leg_b))

def calculate_leg_a(leg_b, hypotenuse):
    return sqrt(sqre(hypotenuse) - sqre(leg_b))

def calculate_leg_b(leg_a, hypotenuse):
    return sqrt(sqre(hypotenuse) - (leg_a))


#Misc Tools

def compare(a, b):
    if a < b:
        return "a is less than b"
    elif a==b:
        return "a equals b"
    elif a>b:
        return "a is greater than b"
    
print(collections_to_dict("USA", "Washington, D.C"))