import csv

with open("priest.csv") as f:       #taking in priest abilities
    reader = csv.reader(f)
    priestly = []
    for a in reader:
        priestly += a
        # print(priestly)

level = 1

yu = input("\tGo through the following information carefully : ")

guide = input("""
    In each instent, you will face a randomly generated enemy.
    Each enemy has its own points, life and damage.
    You have a few abilities that you should use to kill the enemy and protect yourself.
    Whoever kills the other first wins. 
    Be advised to correctly spell your spells or the enemy will take advantage of it.
    
    Good luck
    """)

powers = []

with open("priest.csv") as f:
    reader = csv.reader(f)
    for a in reader:
        powers += reader

x = 1        
for a in powers:
    print("Power", x, "=", a) 
    x += 1


input("\tPress return key to enter your World : ")

def smite(enemyHp):
    enemyHp -= (15 + level*30)
    print(enemyHp)
    return enemyHp

def shield(EliaHp):
    EliaHp += (5 + level*15)
    enemyHp -= (5 + level*15)
    print(EliaHp)
    return EliaHp,

def heal(EliaHp):
    EliaHp += (100 + level*50)
    print(EliaHp)
    return EliaHp

class alienDefinition():
    def __init__(self, bloodColor, points, damage, HP):
        self.bloodColor = bloodColor
        self.points = points
        self.damage = damage
        self.HP = HP
    def attack(self):
        return random.randint(self.damage-10, self.damage+10) 

import random 
points = 0
x = True
level = 1
while x == True:
    
    print("\tlevel", level)
    print("\tYou have been spotted by an enemy !")
    charge = input("\tYou have no choice but to engage !")

    # Generating enemy
    enemy = random.randint(1, 4)

    if enemy == 1:
        alien_0 = alienDefinition("green", 5, random.randint(20, 50), random.randint(300, 400))
    elif enemy == 2:
        alien_0 = alienDefinition("yellow", 10, random.randint(30, 60), random.randint(500, 600))
    elif enemy == 3:
        alien_0 = alienDefinition("blue", 15, random.randint(40, 70), random.randint(700, 800))
    else:
        alien_0 = alienDefinition("red", 25, random.randint(70, 100), random.randint(1200, 1500))

    EliaHP = random.randint(300, 500)

    print("Your HP is ", EliaHP)
    print("Enemy HP is ", alien_0.HP)

    while alien_0.HP > 0 and EliaHP > 0:
        action = input("Enter your command : ")
        if action.lower() == "smite":
            alien_0.HP = smite(alien_0.HP)
            EliaHP -= alien_0.attack()
        elif action.lower() == "shield":
            alien_0.HP -= (5 + level*15)
            pass
        elif action.lower() == "heal":
            EliaHP = heal(EliaHP)
            EliaHP -= alien_0.attack()
        elif action.lower() == "none":
            EliaHP -= alien_0.attack()
        else:
            print("You were confused. The alien played you")
            EliaHP -= alien_0.attack()
        
        print("Elia Hp = ", EliaHP)
        print("Enemy Hp = ", alien_0.HP)
        points += alien_0.points

        if alien_0.HP <= 0:
            print(f"The {alien_0.bloodColor} bloody Victory, you got ", points, " points")
        elif EliaHP <= 0:
            print("You are dead, Game over")
            break
        
    level += 1
    print("level", level)
    uix = input("press enter to continue or 'q' to quite : ")
    if uix == "Q" or uix =="q":
        x = False
    
print("Total points are : ", points)
print("GAME OVER")