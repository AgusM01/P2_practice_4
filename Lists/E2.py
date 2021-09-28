#takes a list and return the sum of every element
#by it's predecesor
#fibonacciList: List -> List
#Takes a list
#Return a list containing the sum of every element
#by his predecesor
#input: [1,2,3] ; output: [1,3,6]
#input: [2,4,6] ; output: [2,6,12]

def fibonacciList():
    c = int(input("Enter the size of the list :"))
    x = 0
    l = []
    #Creating the list
    while x < c:
        n = int(input("Enter the number: "))
        l.append(n)
        x = x + 1
    x = 0
    while x < c:
        if (x == 0):
            l[x] = l[x] #First element
        else:
            k = l[x - 1]
            l[x] = l[x] + k
        x = x + 1
    #print(l)
    return l
fibonacciList()
