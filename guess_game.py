import random
secret =random.randint(1 , 20)
while True:
    guess = int(input("Guess(1 -20):"))
    if guess <secret: print("Too low")
    elif guess > secret : print("Too high")
    else:
        print("Correct!")
        break