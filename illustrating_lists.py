list1=[1,2,3,4,5]
list2=[3,4,5,7,8]
length=len(list1)
str='hello world'
print(list1[0], list1[4], list1[-1], list1[2:4],list1[2:],list1[:2], list1[::2],list1[::-2])
print(str[3:8])
for i1 in list1:
    print(i1,'' ,end='')
print("\n")
for i1 in range(length):
    print(list1[i1],'',end='')
print("\n")

def dotproduct(list1,list2):
    sum=0
    for i1,i2 in zip(list1,list2):
        sum=sum+(i1*i2)
    print(sum)
    return(sum)

dotproduct(list1,list2)

mat1=[[1,2],[3,4]]
mat2=[[4,5],[6,7]]
mat3=[[0,0],[0,0]]

# matrix multiplication using dot product and list comprehension
for i in range(2):
    row=mat1[i]
    for j in range(2):
        col=list([x[j] for x in mat2])
        #print(dotproduct(row,col),'',end='')
        mat3[i][j]=dotproduct(row,col)
print(mat3)

print(list(zip(list1,list2)))
for x in mat2:
    print(x)

alphabets=['c','b','a']
alphabets.sort()
print(alphabets)
alphabets.pop(1)
print(alphabets)

strings=["abc","cdf","efg","bat","can"]
newstring=[x for x in strings if "a" in x]
print(newstring)

