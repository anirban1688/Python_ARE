def sumwhile(n):
    sum=0
    while(n>0):
        sum=sum+n
        n=n-1
    return (sum)

if __name__ == '__main__':
    n=int(input('enter the value: '))
    s=sumwhile(n)
    print(s)

