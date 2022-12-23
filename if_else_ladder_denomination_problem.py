a=[100,50,10,5,2,1]
b=[0,0,0,0,0,0]
n=int(input("Enter the amount: "))
for i in range (6):
    b[i]=n//a[i]
    n=n%a[i]
print("Minimum notes required:")
for i in range (6):
    print("Rs.",a[i],'X',b[i])
