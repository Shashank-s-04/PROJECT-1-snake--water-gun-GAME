'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([1,-1,0])
youstr = input("Enter your choice:")
youDict = {"s":1 , "w":-1 , "g":0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
younum = youDict[youstr]
print(f"You chose {reverseDict[younum]}\nComputer chose {reverseDict[computer ] }")

if(computer==younum):
    print("It's a Draw")
else:
    # if((computer - younum) == - 1 or(computer - younum) == 2 ) :
    #     print("You lose")
    # else:
    #     print("you win")    
    if(computer==-1 and younum ==1):
        print("You Win!")
    elif(computer==-1 and younum ==0):
        print("You Lose!") 

    elif(computer==1 and younum == -1):
        print("You Lose!")
    elif(computer==1 and younum == 0):
        print("You Win!")

    elif(computer==0 and younum==-1):
        print("You Win!")
    elif(computer==0 and younum == 1):
        print("You Lose!")
    else:
        print("Something went wrong")