import random

play = "y"

def context():
    print("You are travelling through the ruins of a castle")
    print("It is overgrown with ivy climbing the walls and ", \
          "rain pouring in through the caved in roof")
    print("Suddenly a knight charges out of the opposite doorway")
    print("They stop and look at you before taking a combat stance")
    print("You must fight")
    print()
    

def playagain():
    play = input("Do you wish to play again? ")
    if play != "y" and play != "n":
        print("Not a valid input")
        play = input("Do you wish to play again? ")
    return play
    print ()

def combat_check(): #defines combat_check func
    #defines Enemy Armour Class
    enemy_ac = int(input("What is the enemies Armour Class? "))
    print()
    playerroll = random.randint(1, 20)

    #prints player roll to screen
    print("You rolled : ", playerroll)
    print()

    #success/miss criteria
    if playerroll == 1:
        print ("Critical fail, your attack goes wide of them")
        print()

    elif playerroll < enemy_ac :
        response = random.randint(1,3)
        if response == 1:
            print("Darn, they dodged the attack")
            print()
            print ("------- end turn -------")
            print()
        if response == 2:
            print("Your opponent has parried the attack")
            print()
            print ("------- end turn -------")
            print()
        if response == 3:
            print("Oh no! you have missed")
            print()
            print ("------- end turn -------")
            

    elif playerroll == 20:
        print("Critical Roll!! You hit for twice the damage")
        print()
        attack_damage(playerroll)
        
        
    elif playerroll >= enemy_ac:
        print("SUCCESS!! You have hit the enemy!!")
        print()
        attack_damage(playerroll)
    


def attack_damage(playerroll):
    print (" ------- Attack Roll -------")
    print ()
    dietype = int(input("How many sides does your attack die have? "))
    print ()
    roll = random.randint(1, dietype)
    if playerroll == 20:
        damage = roll * 2
    else:
        damage = roll

    if damage < 3:
        print("You just clip them with your attack\n")
    elif damage > 3:
        print("Your attack is solid\n")
    elif damage >= dietype:
        print("Your attack has cut deep!\n")

    print("Hit for ", damage, "damage!")

while play == "y":
    context()
    print("------- Start Turn -------")
    print()
    
    combat_check()

    playagain()

else:
    print("Thank you for playing!")
