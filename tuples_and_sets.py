xlist=[1,9,2]
print(xlist)
xtuple=(1,9,2)
print(xtuple)

# lists are mutable, tuples are not
xlist[2]=6
print(xlist)
#xtuple[2]=6
#print(xtuple)

# concatenating lists/tuples
xlist=xlist+[5,2,4]
xtuple=xtuple+(5,2,4)
print(xlist)
print(xtuple)

# assignment to tuples
(x,y)=(5,6)
print((x,y))

# items
thisdict = {
  "a": 1,
  "b": 2,
  "c": 3
}

tuples=thisdict.items()
print(tuples)
# looping over a tuple using items
for (k,v) in thisdict.items():
    print(k,v)

# comparing tuples
check=(0,1,2)<(3,5,6)
print(check)

#using the sorted function
thisdict1 = {
  "c": 1,
  "b": 2,
  "a": 3
}
j=sorted(thisdict1.items())
print(j)

# sorting by values
tmplist=list()
for (k,v) in thisdict.items():
    tmplist.append((v,k))

print(tmplist)
tmplist=sorted(tmplist,reverse=True)
print(tmplist)

thisset={"a","b","c"}
thisset.add("d")
print(thisset)
thisset.update(["e","f","g"])
print(thisset)