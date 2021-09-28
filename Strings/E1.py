#Takes a string and show every character
#everyCharacter: String -> String
#Takes a string
#Return every character from the beggining to the end
#input: hello ; output: h
#                       e
#                       l
#                       l
#                       o
#input: agus ; output: a
#                      g
#                      u
#                      s

def everyCharacter():
    s = list(input("Enter the string: "))
    x = 0
    for x in s:
        print(x)

everyCharacter()

