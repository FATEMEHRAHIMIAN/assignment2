

bord =0
bakht =0
mosavi =0
emtiyaz = 0
count =1

#5 team -> bargashti -> 10 tiem 
# 2 bar khod team imamreza---------->>>> 10 - 2 = 8 >>>> count <9
while count <9 :
    print("Enter play football", count ) 
    print( "bord->1 \t mosavi->2 \t bakht ->3" )
    play = int(input("natije bazi? "))
    if play == 1 :
        bord += 1
        emtiyaz += 3
    elif play == 2 :
        mosavi +=  1
        emtiyaz += 1
    elif play == 3 :
        bakht += 1
        emtiyaz += 0
    else :
        print("try again.. ")
        count -= 1
    count += 1
print(" emtiyaz = ",emtiyaz )
print("bord = :) ", bord)
print("tedad mosavi = ", mosavi)
print("bakht = ",bakht)
