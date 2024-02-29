def printStar(n):
    if n==1:
        return print('*')
    else:

        printStar(n-1)
        return print('*'*n)

printStar(5)