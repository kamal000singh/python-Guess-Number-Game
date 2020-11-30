print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
cmb_string=name1+name2
cmb_string=cmb_string.lower()
true=cmb_string.count("t")+cmb_string.count("r")+cmb_string.count("u")+cmb_string.count("e")
love=cmb_string.count("l")+cmb_string.count("o")+cmb_string.count("v")+cmb_string.count("e")
love_score=int(str(true)+str(love))
if(love_score>40 and love_score<50):
  print(f"Your love score is {love_score}, you are alright together.")
elif(love_score<10 or love_score>90):
  print(f"Your love score is {love_score}, you go together like coke and mentos.")
else:
  print(f"Your love score is {love_score}.")
