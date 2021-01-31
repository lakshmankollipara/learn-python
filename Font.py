## This logic can be written in different ways. But, the core concept is the String slicing (str[start:end])
##Refer to this page for more details: https://www.w3schools.com/python/gloss_python_string_slice.asp


def firstTwo(str):                                           ##This functions takes the first two characters as input
    if str[:1].lower() == 'a' and str[1:2].lower() == 'b':   ##Checks if the first character is a and second character is b
        return str[:2]                                       #if Yes, returns the first two characters
    elif str[:1].lower() == 'a':                             #if 1st condition is not met, checks if first character is a (second character can be anything)
        return str[:1]                                       #if Yes, returns the first character
    elif str[1:2].lower() == 'b':                            #if 2nd condition is not met, checks if second character is b (first character can be anything)
        return str[1:2]                                      #if Yes, returns the second character
    else:
        return ""                                            #If none of the above conditions  (if first 2 characters are not a and b/ a or b, returns empty string


def deFont(str):
    first_two = firstTwo(str[:2])               ##Take first two characters of a string
    sliced = str[2:]                            ##Take the rest of the string excluding first two characters
    print('"' + first_two + sliced + '"')       ## Concat (add) the return value of first-two function and remaining string.


print("deFont Function")

deFont("Hello")
deFont("java")
deFont("away")
deFont("*Beautiful")
deFont("Beautiful")
deFont("aB")
deFont("xB")
deFont("a")
deFont("B")