#Take a list and eliminate the first and the last element
#eliminate_ List -> List
#Take a list
#Return the list without it's first and last element
#input:[1,2,3,4]; output:[2,3]
#input:[a,b,c,d,s]; output:[b,c,d]

def eliminate():
    s = int(input("Enter the size of the list: "))
    l = []
    x = 0
    #Creating the list
    for x in range (s):
        n = int(input("Enter a number: "))
        l.append(n)
    #Eliminating elements
    x = 0   
    for x in range (s):
        if(x == 0):
            del l[x]
        elif (x == (s - 2)): #It ends in s - 1
            del l[x]
        else:
            l = l
    #print(l)
    return l
eliminate()
