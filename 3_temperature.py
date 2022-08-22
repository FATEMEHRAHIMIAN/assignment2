k=0
f=0
c=0

temperature =int(input("Which one you need? \n C->F   1 \n K->F   2 \n C->K   3 \n F->C   4 \n F->K   5 \n K->C   6 \n"))
if temperature == 1:
        c=float(input("Enter your Celsius.. "))
        f=(c*9/5)+32
        print(c, "Celsius to Fahrenheit is", f)
elif temperature == 2 :
        k = float(input("Enter your Kelvin.."))
        f = 9/5(k - 273)+32
        print(k ,"Kelvin to Fahrenheit is ",f)
elif temperature == 3:
        c=float(input("Enter your Celsius.. "))
        k=c+273
        print(c, "Celsius to kelvin is", k)
elif temperature == 4 :
        f=float(input("Enter your Fahrenheit.. "))
        c = (f-32)*5/9
        print(f, "Fahrenheit to Celsius is", c)
elif temperature == 5 :
        f=float(input("Enter your Fahrenheit.. "))
        k = (f + 459)*5/9
        print(f, "Fahrenheit to kelvin is", c)
elif temperature == 6 :
        k = float(input("Enter your Kelvin.."))
        c= k - 273
        print(k, " kelvin  to Celsius  is", c)
else:
        print("try again ..")