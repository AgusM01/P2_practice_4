#takes a list and return a boolean depending if a value 
#appears duplicate in it
#duplicate: List -> Boolean
#Take a list
#Return True if it has a duplicated element
#Return False if not
#Input: [1,2,3,4]; Output: False
#Input: [a,a,b,c]; Output: True

def duplicate():
    s = int(input("Enter the size of the list: "))
    l = []
    x = 0
    #Creating the list
    for x in range (s):
        n = input("Enter an element: ")
        l.append(n)
    x = 0 #Value for the first for loop
    a = 0 #Counter a
    y = 0 #Counter y
    k = 0 #Value for the second for loop
    for x in range (s):
        if x > 0:
            d = l[x]
            for k in range (s): #Compare the element with all the list
                if (d == l[k]):
                    a = a + 1 # a is the amount of times the number appears
                if (a >= 2): # >= 2 to not count the number itself
                    return True     
        a = 0 #Restart the counter
        return False

duplicate()

