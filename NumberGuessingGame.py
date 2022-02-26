import random

number = random.randint(0,10)
yourNumber =  input("Guess your number here: ")

if(yourNumber == number):
    print("COngrats you have won")
else:
    print("your guess was too low try entering a different number next time")