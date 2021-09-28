#Counts how many times a character x appears in a string
#counting String, String (letter) -> Int
#Takes 1 string and 1 character
#Return how many times the character appears
#in the string
# input: hello, l; output: 2
# input: computer, e; output: 1

def counting ():
    s = list(input("Enter the string: "))
    c = (input("Enter the character: "))
    x = 0
    t = 0
    for x in s:
        if x == c:
            t = t + 1
    #print(t)
    return t

counting()
