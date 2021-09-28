#Count how many times a vowel appears in a string
#vowels: String --> Int
#Takes a string
#Return an int representing how many times 
#a vowel was in the string
#input: hello;  output: 2
#input:cOmpUter; output: 3
import string
def vowels():
    a = list(string.ascii_letters)
    y = 0
    v = []
    for y in a:
        if ((y == "a") or
            (y == "e") or
            (y == "i") or
            (y == "o") or
            (y == "u") or
            (y == "A") or
            (y == "E") or
            (y == "I") or
            (y == "O") or
            (y == "U")):
            
            v.append(y)
    s = list(input("Enter the string: "))
    x = 0
    cv = 0
    for x in s:
        for y in v:
            if (x == y):
                cv = cv + 1
    #print (cv)
    return cv

vowels()
