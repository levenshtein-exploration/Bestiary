import os
from itertools import product, repeat

with open("resultats.txt","w") as f:
    f.write("")
    
with open("resultats2.txt","w") as f:
    f.write("")

k=5 #distance
a=2 #taille de l'alphabet
n=10 #taille des mots

iteration=product("abcd",repeat=n)
liste_mots=[]

for element in iteration:
    liste_mots.append(str(element).replace("', '","").strip("('')"))

for element in liste_mots:
    for element2 in range(1,k+1):
        os.system("srun --qos=fast --partition=common,dedicated ./wordborhood -d dula"+str(element2)+".fsm -a "+str(a)+" -k "+str(element2)+" "+element+" >> resultats.txt")

with open("resultats.txt","r") as f:
    lines=f.readlines()

with open("resultats2.txt","a") as f:
    l=0
    for element in liste_mots:
        for element2 in range(1,k+1):            
            if(element2==1):
                f.write(lines[l].strip())
            elif(element2==k):
                f.write(lines[l].strip(element))
            else:
                f.write((lines[l].strip()).strip(element))
            l+=1

os.system("rm resultats.txt")
os.system("mv resultats2.txt resultats.tsv")