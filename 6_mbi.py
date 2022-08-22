
height = float(input("Enter your height.. metra "))
Weight = float(input("Enter your Weight..  kg "))
height_2 = height*height
bmi = Weight/(height**2)
print("bmi is ",bmi)
if 16 <bmi<18.5:
        print("body Weight deficit..")
elif 18.5<bmi<24:
        print("norm")
elif 24<bmi<30:
        print("Weight over")
elif 30< bmi <35:
        print("obesity first degree")
    