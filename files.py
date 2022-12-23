# f = open("test.txt",'w')
import os
import json # java script object notation. platform independent
import csv

with open("test.txt", 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")
    f.close()

# reading from a line and counting the lines
fhand = open('test.txt', 'r')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)
f.close()

# read command --- reads the entire file in a string
fhand = open('test.txt', 'r')
inp = fhand.read()
print(inp)
print(len(inp))
f.close()

# searching in a file
fhand = open('test.txt', 'r')
for line in fhand:
    if line.startswith('my'):
        print(line)
f.close()

fhand = open('test.txt','r')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('my'):
        continue
    print(line)
f.close()

# opening files through the input command
fname=input(' Enter the file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('my'):
        print(line)
f.close()

# file append
f=open('test.txt','a')
f.write('Adding some more contents \n')
f.close()

f=open('test.txt','r')
print(f.read())
f.close()

# check if a file exists on a path
print(os.path.exists('test.txt'))

# exporting dictionaries
dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
# create json object from dictionary
json = json.dumps(dict)

# open file for writing, "w"
f = open("dict.json","w")


# write json object to file
f.write(json)
# close file
f.close()


with open('test.csv', 'w') as f:
    for key in dict.keys():
        f.write("%s,%s\n"%(key,dict[key]))
f.close()