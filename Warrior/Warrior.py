import random
import csv
print("Hellow WOrld!")
# dutring the pendamic.

Specs = []
with open("Warrior.csv") as f:
    a = csv.reader(f)
    for x in a:
        Specs.append(x)
    del Specs[0]
print(Specs)

# Instruction to play the game
yu = input("\tGo through the following information carefully : ")

guide = input("""
    In each instent, you will face a randomly generated enemy.
    Each enemy has its own points, life and damage.
    You have a few abilities that you should use to kill the enemy and protect yourself.
    Whoever kills the other first wins. 
    Be advised to correctly spell your spells or the enemy will take advantage of it.
    
    Good luck
    """)

x = 1
for a in Specs:
    print("Power", x, "=", a)           # Instructions on details of abilities
    x += 1

input("\tPress return key to enter your World : ")


class Enemy():                              # Enemy generation tamplate
    def __init__(self, damage, HP, point, species):
        self.damage = damage
        self.HP = HP
        self.point = point
        self.species = species

    def attack(self):
        return random.randint(self.damage - 10, self.damage+50)


Enemy1 = Enemy(40, random.randint(300, 400), 5, "Slime")
Enemy2 = Enemy(70, random.randint(400, 550), 10, "Goat")
Enemy3 = Enemy(80, random.randint(550, 700), 15, "Lion")
Enemy4 = Enemy(100, random.randint(900, 1200), 25, "Minotor")

x = random.randint(1, 4)

if x == 1:
    y = Enemy1
elif x == 2:
    y = Enemy2
elif x == 3:
    y = Enemy3
elif x == 4:
    y = Enemy4


class Charactor():
    def __init__(self, HP, Damage):
        self.HP = HP
        self.Damage = Damage


Warrior = Charactor(random.randint(500, 700), 70)

print(f"A {y.species} jumps out of the bushes.")

print("Your HP is :", Warrior.HP)
print(f"{y.species} HP is :", y.HP)

print("You charged at the enemy, enemy misses its first turn.")
x = input()
y.HP -= random.randint(Warrior.Damage , Warrior.Damage + 70 )

print("Warrior's HP = ", int(Warrior.HP))
print(f"{y.species}'s HP = ", int(y.HP))

ability = input("What are you gonna do? : ")

if ability == "rage":
    print("You used Rage ability, increases your damage and attack twice")
    y.HP -= 1.2 * Warrior.Damage
    print()
    y.HP -= 1.2 * Warrior.Damage
    Warrior.HP -= random.randint(y.damage-15, y.damage+15)
    print("Warrior's HP = ", int(Warrior.HP))
    print(f"{y.species}'s HP = ", int(y.HP))
elif ability == "bash":
    print("Enemy is stunned for 2 turns")
    y.HP -= 0.5 * Warrior.Damage

    
