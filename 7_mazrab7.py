

num=int(input("Enter your number.. "))
if num % 7 == 0:
    print("Your number is Multiple 7 ...")
else:
    after = 7 - num % 7 + num
    print("Multiple 7 after your number is", after)