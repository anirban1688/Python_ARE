# This is a Python script to solve a quadratic equation using inputs from the user.
# This code uses the math library of python for the square root function sqrt()
# Exhibits the use of 'input' function of python
# Exhibits type casting
# Exhibits special condition checks

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def sol_quad(a,b,c):
    # Use a breakpoint in the code line below to debug your script.
    print('Executing function to solve a quadratic equation')


    disc=b*b-4*a*c
    if disc<0: # taking care of the complex roots when the discriminant is less than zero
        disc=math.fabs(disc)
        sq_root_disc=math.sqrt(disc)
        real_val=-(b/(2*a))
        im_val=(sq_root_disc/(2*a))
        print(real_val,im_val)
        print(real_val,-im_val)
    else:
        sol1=(-b+math.sqrt(disc))/(2*a)# Press Ctrl+F8 to toggle the breakpoint.
        sol2=(-b-math.sqrt(disc))/(2*a)
        print('first root:',sol1)
        print('second root:',sol2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Enter the coefficients of the quadratic equation')
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    if (a == 0):
        print ('Leading coefficient is zero')
        print('sol=',-b/c)
    else:
        sol_quad(a,b,c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
