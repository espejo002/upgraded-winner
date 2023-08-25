#A quadratic equation calculator on Python
from math import*
try:
    a= float(input("Input the coefficient of x-square(x^2): "))
    b= float(input("Input the coefficient of x(x^1): "))
    c= float(input("Input the constant of the equation(x^0): "))
    d= float(b)*-1
    e= pow(float(b), 2)
    f= 4*float(a)*float(c)
    g= float(e)-float(f)
    if g<0:
        print("Can't Solve Equation")
    h= (sqrt(float(g)))
    x_plus= (float(d)+float(h))/(2*float(a))
    x_minus= (float(d)-float(h))/(2*float(a))
    print("x= " +str(x_plus)+ " or " +str(x_minus))
    print("
")
except ValueError:
    print("Invalid Input. Try entering a number")

