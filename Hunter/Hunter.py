# This is the third string of the same game, designed on the same engine
import csv
import random

# importing stats
Stats = []
with open("./hunter/Hunter.csv") as f:
    x = csv.reader(f)
    for d in x:
        Stats.append(d)
    del Stats[0]
print(Stats)

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
for a in Stats:
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

class Charactor():                              # Charactor generation template
        def __init__(self, HP, Damage):
            self.HP = HP
            self.Damage = Damage

points = 0
asd = ""
Hunter = Charactor(random.randint(300, 400), random.randint(100,120))           # Charactor defining

while asd.lower() != "q":

    x = random.randint(1, 4)

    # Enemy defining
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

    print(f"{y.species} HP is :", y.HP)
    print("Your HP is :", Hunter.HP)
    
    print("\nWhat are you gonna do? : ")

    x = 0

    while Hunter.HP > 0 and y.HP > 0:       # First level loop, enters into battle with a new monster

        ability = input("Spell your next move : ")

        if ability.lower() == "poison":        # The whole full loop was made just if poison was active.
            x = 5
            while x > 0 and Hunter.HP > 0 and y.HP > 0:
                y.HP -= 0.5 * Hunter.Damage
                points += y.point
                x -= 1
                print(f"{y.species} HP is : ", y.HP)
                print("Hunter's HP is : ", Hunter.HP)

                ability = input("Spell your next move : ")

                if ability.lower() == "strike":
                    y.HP -= Hunter.Damage
                    points += y.point
                    Hunter.HP -= y.damage
                    print(f"{y.species} HP is : ", y.HP)
                    print("Hunter's HP is : ", Hunter.HP)
                elif ability.lower() == "playdead":
                    print("The Enemy thought you dead and left")
                    print("YOur points are : ", points)
                    break
                else:
                    print("Enemy had you confused and wasted no chance to strike you.")
                    Hunter.HP -= y.damage
                    print(f"{y.species} HP is : ", y.HP)
                    print("Hunter's HP is : ", Hunter.HP)

        elif ability.lower() == "strike":
            y.HP -= Hunter.Damage
            points += y.point
            Hunter.HP -= y.damage
            print(f"{y.species} HP is : ", y.HP)
            print("Hunter's HP is : ", Hunter.HP)
        elif ability.lower() == "playdead":
            print("The Enemy thought you dead and left")
            print("YOur points are : ", points)
            break
        else:
            print("Enemy had you confused and wasted no chance to strike you.")
            Hunter.HP -= y.damage
            print(f"{y.species} HP is : ", y.HP)
            print("Hunter's HP is : ", Hunter.HP)

        if y.HP <= 0:
            print(f"Victory, You have defeated {y.species}, your current points are {points}")
        elif Hunter.HP <= 0:
            print("You have died")
            print("Total score is : ", points)
            print("GAME OVER")
            break
    
    asd = input("Press entre to continue, or 'Q' to quite : ")

print("Total score is : ", points)
points = 0
print("GAME OVER")
        



