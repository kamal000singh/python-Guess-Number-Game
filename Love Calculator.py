print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1=name1.lower()
name2=name2.lower()
c1=name1.count("t")+name1.count("r")+name1.count("u")+name1.count("e")+name2.count("t")+name2.count("r")+name2.count("u")+name2.count("e")
c2=name1.count("l")+name1.count("o")+name1.count("v")+name1.count("e")+name2.count("l")+name2.count("o")+name2.count("v")+name2.count("e")
c=str(c1)+str(c2)
s=int(c)
if(s>40 and s<50):
  print(f"Your score is {s}, you are alright together.")
elif(s<10 or s>90):
  print(f"Your score is {s}, you go together like coke and mentos.")
else:
  print(f"Your score is {c}.")
