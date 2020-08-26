# # # Same program was build second time for warrior


import random
import csv

Specs = []
with open(".\Warrior\Warrior.csv") as f:        # Taking abilities' details out from the CSV file
    a = csv.reader(f)
    for x in a:
        Specs.append(x)
    del Specs[0]
print(Specs)

# Instruction to play the game
yu = input("\tGo through the following information carefully : ")

guide = input("""
    In each instence, you will face a randomly generated enemy.
    Each enemy has its own points, life and damage.
    You have a few abilities that you should use to kill the enemy and protect yourself.
    Kill your foe to continue your adventure. 
    Be advised to correctly spell your abilities or the enemy will take advantage of it.
    
    Good luck
    """)

x = 1
for a in Specs:
    print("Power", x, "=", a)           # Instructions on details of abilities
    x += 1

input("\nPress return key to enter your World : \n")


class Enemy():                              # Enemy generation tamplate
    def __init__(self, damage, HP, point, species):
        self.damage = damage
        self.HP = HP
        self.point = point
        self.species = species

    def attack(self):
        return random.randint(self.damage - 10, self.damage+50)

class Charactor():
        def __init__(self, HP, Damage):
            self.HP = HP
            self.Damage = Damage

points = 0
asd = ""
Warrior = Charactor(random.randint(500, 700), 70)

while asd.lower() != "q":               # Generating a random enemy

    x = random.randint(1, 4)

    Enemy1 = Enemy(40, random.randint(300, 400), 5, "Slime")
    Enemy2 = Enemy(70, random.randint(400, 550), 10, "Goat")
    Enemy3 = Enemy(80, random.randint(550, 700), 15, "Lion")
    Enemy4 = Enemy(100, random.randint(900, 1200), 25, "Minotor")

    if x == 1:
        y = Enemy1
    elif x == 2:
        y = Enemy2
    elif x == 3:
        y = Enemy3
    elif x == 4:
        y = Enemy4

    

    print(f"A {y.species} jumps out of the bushes.\n")

    print("Your HP is :", Warrior.HP)
    print(f"{y.species} HP is :", y.HP)

    print("\nYou charged at the enemy, enemy misses its first turn.")
    x = input()
    y.HP -= random.randint(Warrior.Damage , Warrior.Damage + 70 )

    print("Warrior's HP = ", Warrior.HP)
    print(f"{y.species}'s HP = ", y.HP)
    

    print("\nWhat are you gonna do? : ")

    while Warrior.HP > 0 and y.HP > 0:              # Fight with each monster starts from here

        ability = input("Your move for the next turn : ")

        if ability == "rage":
            print("You used Rage ability, increases your damage and you attack twice")
            y.HP -= 1.2 * Warrior.Damage
            points += y.point
            print()
            y.HP -= 1.2 * Warrior.Damage
            points += y.point
            Warrior.HP -= random.randint(y.damage-15, y.damage+15)
            print("Warrior's HP = ", Warrior.HP)
            print(f"{y.species}'s HP = ", y.HP)
            print(points)

        elif ability == "bash":
            print("Enemy is stunned for this turns")
            y.HP -= 0.5 * Warrior.Damage
            points += y.point
            print("Warrior's HP = ", Warrior.HP)
            print(f"{y.species}'s HP = ", y.HP)
            print(points)

        else:
            print("You got confused. Enemy wasted no chance to make use of it.")
            Warrior.HP -= random.randint(y.damage-15, y.damage+15)
            print("Warrior's HP = ", int(Warrior.HP))
            print(f"{y.species}'s HP = ", int(y.HP))
            print(points)

        
    if y.HP <= 0:
        print(f"Victory, You have defeated {y.species}, your current points are {points}")
    elif Warrior.HP <= 0:
        print("You have died")
        break
    
    asd = input("Press entre to continue, or 'Q' to quite : ")

print(f"Total score is : ", points)
print("GAME OVER")                              # Game ends

