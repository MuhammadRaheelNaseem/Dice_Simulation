import random

while 1:
    print("""1.) Roll The Dice \n2.) Exit  """)
    user = int(input("what you want to do \n"))
    if user==1:
        number = random.randint(1,6)
        print("Dice-----> ",number)
    else:
        break
