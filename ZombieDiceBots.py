print('NAME:vikas gm' ,'USN:1AY24AI115') 
import random 
dice=['brain','brain','brain','footsteps','footsteps','shot'] 
def roll(): 
    return random.choice(dice) 
def zombie_dice_bot(): 
    brains=0 
    shots=0 
 
    while shots < 2: 
        result=roll() 
        print("rolled:",result) 
 
        if result=='brain': 
            brains +=1 
        elif result == 'shot': 
            shots += 1 
        if shots >= 2: 
            print("too many shots! stop rolling.") 
            break 
    print("brains collected:",brains) 
zombie_dice_bot()