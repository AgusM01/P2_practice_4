#takes a list and a number and return the list of the elements 
#which are in the positions of the number's multiples
#positionsMultiple: List Num --> List
#takes a list and a number
#return the list of the elements 
#which are in the positions of the number's multiples
#input: ([1,2,3,4,5,6,7],2) ; output: [1,3,5,7]
#input: ([1,2,3,4,5,6,7],3) ; output: [1,4,7]

def positionsMultiples():
    s = int(input("Enter the size of the list: "))
    l = []
    x = 0
    #Creating the list
    for x in range (s):
        n = int(input("Enter a number: "))
        l.append(n)
    #Selecting the multiple positions
    x = 0
    y = int(input("Enter the number to select the multiples: "))
    for x in range (s):
        if (y % (x + 1)) == 0:
            l = l
        else:
            del l[x]
    #print (l)
    return l


positionsMultiples()


