import random

janr = int(input("1.Film\n2.Anime\n3.Serial\n"))

if janr==1:
    name = "films.txt"
if janr==2:
    name = "anime.txt"
if janr ==3:
    name = "soap.txt"

with open(name, 'r', encoding="utf-8") as f:
    list_of = f.readlines()
    

print(random.choice(list_of))
