#Takes a list and return a boolean 
#order: List -> Boolean
#Take a list
#Return True if the elements are in ascedent order
#Return False if not
#input:[1,2,3,4]; output: True
#input:[b,a]; output: False
import string

def order():
    s = list(string.ascii_lowercase) #Creates a list with the alphabet in it
    #it is like s = [a,b,c,d,...,z]
    c = int(input("Enter the size of the list :"))
    x = 0
    l = []
    #Creating the list
    while x < c:
        n = input("Enter the number: ")
        l.append(n)
        x = x + 1
    x = 0
    a = 0
    while x != c:
        if(x == 0):
            x = x + 1
        else:
            if(l[x] > l[x-1]) or (l[x] == s[x]):
                a = a + 1
                x = x + 1
            else:
                x = x + 1
    if (a == (x - 1)):
        return True
    else:
        return False
    
order()

            
