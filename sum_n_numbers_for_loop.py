def sum(n):
    add=0
    for i in range(1,n+1):
        add=add+i
    return(add)

if __name__ == '__main__':
    n=int(input("enter the limit "))
    total=sum(n)
    print('The sum of the first',n,'natural numbers is',total)