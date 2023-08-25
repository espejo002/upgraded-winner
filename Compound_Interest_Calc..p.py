#A Calculator to Calculate Compound Interest
from math import*
try:
    
    a= input("Enter your currency:
")
    b= float(input("Enter the Principal:
" +a))
    c= float(input("Enter the Rate(do not put the % sign):
"))
    d= float(input("Enter the Time/Period(in terms of years):
"))
    e = 1+(float(c)/100)
    f = pow(float(e), float(d))
    g = float(f)*float(b)
    h = float(g)-float(b)
    print('Compound Interest is ' +a+str(h))
    print('Amount is ' +a+str(g))
except ValueError:
    print("Error! Invalid Input. Try Entering a number")


