from itertools import count


username = "Fatemeh"
password = '1234'
counter =3
while counter <4:
    user = input("Enter your username")
    password_us=input("Enter your pass")
    if user == username and password_us == password :
        print("successful..")
        continue
    elif counter ==  1:
        print("blocked..")   
    else:
     print("try  again..")
     counter = counter - 1