#Decides if a word is part of a list using binary search
#binarySearch: List String -> Boolean
#Takes a list IN ALPHABETICAL ORDER and a string
#Return True if the string is part of the list
#Return False if not
#Uses binary search
#input: [agus, be, cloud], cloud ; output: True
#input: [atmosphere, qbit, virtual], computer ; output: False
from math import *
import string
def binarySearch():
    s = int(input("Enter the size of the list: "))
    l = []
    x = 0
    #Creating the list
    for x in range (s):
        n = input("Enter an element: ")
        l.append(n)
    w = input("Enter the word to search: ")
    a = list(string.ascii_lowercase)
    lw = list(w)
    y = 0
    fh = 0
    sh = 0
    for y in range (0,13) :
        if lw[1] == y:  #First letter between A and M --> First half
            fh = 1
        else:           #First letter between N and Z --> Second half 
            sh = 1
    x = 0
    t = 0
    hfs = floor(s/2)
    if fh == 1:
        for x in range (0,hfs):
            if w == l[x]:
                t = 1
        if t == 1:
            print("t")
            return True
        else:
            print("f")
            return False            
    elif sh == 1:
        x = 0
        for x in range (hfs,s):
            if w == l[x]:
                t = 1
        if t == 1:
            print("t")
            return True
        else:
            print("f")
            return False
    else:
        print("F")
        return False

binarySearch()
