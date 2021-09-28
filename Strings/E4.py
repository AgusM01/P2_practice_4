#Takes a string of words separates by spaces and return
#how many words of more than five letters are
#words_FiveLetters: String -> Int
#Takes a string
#Return how many words with more than five letters are
#input: 'hello world'; output: 2
#input: 'i love computer science'; output: 2

def words_Fiveletters():
    s = list(input("Enter the string: "))
    x = 0
    c = 0
    tc = 0
    for x in s:
        if x != ' ':
            c = c + 1
        if c == 5:
            tc = tc + 1
    #print (tc)
    return tc

words_Fiveletters()
