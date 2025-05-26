print('NAME:vikas gm' ,'USN:1AY24AI115')
import random
number=random.randint(1,100)
guess=int(input("guess the number between 1 and 100:"))
if guess==number:
    print("you guessed it!!")
else:
    print(f"wrong! the number was {number}")
