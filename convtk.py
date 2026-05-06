
'''
Welcome to the convtk, or "Convenience Toolkit". This is a project of mine meant to take away all of the stacked code and let you
code faster and more readable.
Main Contributor: Fastpast93
'''
#Custom Errors
class ModeError(Exception):
    pass
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

def mul_title(collection): # <--Takes a List or Tuple and returns the collection with all of the words capitalized
    output = []
    for string in collection:
        output.append(string.title())
    return output 


#Dict Tools

def key_value_separator(dict): # <-- Takes a Dict and returns a 2D list of keys and values.
    keys, values = [], []
    for key, value in dict.items():
        keys, values = keys.append(key), values.append(value)
    return [keys, values]
    
#Math Tools

def sqrt(num=0): # <-- Takes a number and returns its square root
    return num ** 0.5

def parity(num=0): # <-- Takes a number and returns if it's even or odd
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
def sqre(num=0): # <-- Takes a number and returns the square
    return num ** 2

def calculate_hypotenuse(leg_a=0, leg_b=0): # <-- Takes leg a and leg b of a right triangle and returns the hypotenuse
    return sqrt(sqre(leg_a)) + (sqre(leg_b))

def calculate_leg_a(leg_b=0, hypotenuse=0): # <-- Takes leg b and the hypotenuse and returns leg a
    return sqrt(sqre(hypotenuse) - sqre(leg_b))

def calculate_leg_b(leg_a=0, hypotenuse=0): # <-- takes leg a and the hypotenuse and returns leg b
    return sqrt(sqre(hypotenuse) - (leg_a))

def num_cleaner(num): # <-- Takes a number and decides if it should be a float or integer
    if num == int(num):
        return int(num)
    else:
        return num

    

#File Tools

def clean_path(file_path=""): # <-- Takes a file path and cleans it so it can be inserted directly into a file path lookup
    return mul_replace(file_path, {'\\':'/', '"':''})

def ez_file(file_path, mode="read", text=""): # <-- Takes a file path and a mode (read, write) and does the mode to the file. If writing, use the text arg
    match mode.lower():
        case "read":
            with open((clean_path(file_path)), "r") as f:
                return f.read()
        case "write":
            with open((clean_path(file_path)), "w") as f:
                f.write(text)
        case _:
            raise ModeError(f"From convtk: Expected read, write, as a mode but instead was given \"{mode}\"")

def ez_json(file_path, mode="read", text=""): # <-- Takes a json file path and a mode (read, write) and does the mode to the file. If writing, use the text arg
    try:
        match mode.lower():
            case "read":
                with open((clean_path(file_path)), "r") as f:
                    return json.load()
            case "write":
                with open((clean_path(file_path)), "w") as f:
                    json.dump(text)
            case _:
                raise ModeError(f"From convtk: Expected read, write, as a mode but instead was given \"{mode}\"")
    except NameError:
        import json
        match mode.lower():
            case "read":
                with open((clean_path(file_path)), "r") as f:
                    return json.load()
            case "write":
                with open((clean_path(file_path)), "w") as f:
                    json.dump(text)
            case _:
                raise ModeError(f"From convtk: Expected read, write, as a mode but instead was given \"{mode}\"")