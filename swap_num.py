# this is a code to swap two numbers without using a third variable
# objective: logic development
# illustration of expression assignment


def swap(a,b):
    print('Now swapping the values of a and b')
    a=a+b
    b=a-b
    a=a-b
    print('a:',a)
    print('b:',b)


if __name__ == '__main__':
    a=int(input('a:'))
    b=int(input('b:'))
    swap(a,b)