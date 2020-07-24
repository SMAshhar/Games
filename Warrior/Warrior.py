print("Hellow WOrld!")
#dutring the pendamic.
import csv

with open("Warrior.csv") as f:
    a = csv.reader(f)
    Specs = []
    for x in a:
        Specs.append(x)
print(Specs)