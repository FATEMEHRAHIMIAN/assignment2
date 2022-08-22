odd = 0 #fard
even =0 #zoj
num = int(input("Enter a integer number please ... "))
while num > 0:
    number = num % 10
    num //= 10
    if number % 2 ==0 or number ==0:
        even = even+1
    else:
        odd = odd+1
if odd > even:
    print(" odd > even in your number :)")
elif odd ==even:
    print(" odd = even in your number :)")    
else:
    print("even > odd in your number :)")