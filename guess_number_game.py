import random
n = random.randint(1,100)
count=1
print("Guess your number (1-100)")
print("You have only 9 attempt ")
while(True):
    a=int(input("Enter your guess "))
    if(a==n):
        remain = 9 - count
        print("you guess correct \nGuess attempt :",count,"Remaining:",remain)
        break
    elif(count==9):
        print("GAME OVER")
        break
    elif(a<n):
        print("guess greater number")
        count=count + 1
    else:
        print("guess lesser number")
        count = count + 1