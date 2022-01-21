
def bruteForce(n): #this bruteforces and finds the number
    b = ''
    for a in range (1,n+1):
        b += str(a)
    return b[n-1]

def mult10(x): # x will be an integer and it will be the exponent for n later on
    a = 1
    object = 0
    for tens in range (x):
        object = 10**tens
        a *= int(bruteForce(object))
    return a 


if __name__ == "__main__": 
    print (mult10(7))

