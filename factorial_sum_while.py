def factorial(n):
    fac=1
    while(n>0):
        fac=fac*n
        n=n-1
    return (fac)

def sum(n):
    add=0
    while(n>0):
        add=add+n
        n=n-1
    return (add)

if __name__ == '__main__':
    n=int(input("enter the limit "))
    total=sum(n)
    fac=factorial(n)
    print('The sum and factorial of the first',n,'natural numbers is',total,fac)