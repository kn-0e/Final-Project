def bruteForce(n):
    b = ''
    for a in range (1,n+1):
        b += str(a)
    return b[n-1]

if __name__ == "__main__": 
    n = 10**6
    print (bruteForce(n))

