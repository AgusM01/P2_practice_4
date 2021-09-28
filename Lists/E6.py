#takes a list and return the list without the duplicate objects in it
#duplicate: List -> List
#Take a list
#Return a new liste whithout the duplicated element
#Return the same list if not
#Input: [1,2,3,4]; Output: [1,2,3,4]
#Input: [a,a,b,c]; Output: [a,b,c] 

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
    p = []
    z = 0
    w = 0
    nl = []
    for x in range (s):
        if x > 0:
            d = l[x]
            for z in (p): #Verify if the element was previously checked
                if (d == z):
                    w = 1
            if (w != 1):
                for k in range (s): #Compare the element with all the list
                    if (d == l[k]):
                        a = a + 1 #a is the amount of times the number appears
                    if (a >= 2): #>= 2 to not count the number itself
                        y = 1    #Flag 
                        p.append(l[x])
                    else: #Case non-repeated elements
                        y = 3  
                if (y == 1) or (y == 3):
                    nl.append(l[x])
                    y = 0    
        w = 0 #Restart the counter   
        a = 0 #Restart the counter
    print (nl)
    return nl
duplicate()

