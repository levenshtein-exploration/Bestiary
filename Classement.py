import os
import argparse
import string
import subprocess
from itertools import product, repeat

parser = argparse.ArgumentParser()
parser.add_argument("-a", type=int, default=2)
parser.add_argument("-n", type=int, default=4)
parser.add_argument("-k", type=int, default=2)
args = parser.parse_args()

with open("resultats.txt","w") as f:
    f.write("")
with open("resultats2.txt","w") as f:
    f.write("")
with open("temp.txt","w") as f:
    f.write("")

k=args.k #distance
a=args.a #taille de l'alphabet
n=args.n #taille des mots
m=pow(a,n) #number of words

alphabet=""
for lettre in list(map(chr, range(ord("a"), ord("a")+a))):
    alphabet+=lettre

iteration=product(alphabet,repeat=n)
liste_mots=[]

for element in iteration:
    liste_mots.append(str(element).replace("', '","").strip("('')"))
    
with open("temp.txt","a") as f:
    for mot in liste_mots:
        f.write(mot+"\n")

for distance in range(1,k+1):
    #subprocess.call(["wordborhood.cpp","-d","dula"+str(distance)+".fsm","-a",str(a),"-k",str(distance),"-w","temp.txt"])
    os.system("srun --qos=fast --partition=common,dedicated ./wordborhood -d dula"+str(distance)+".fsm -a "+str(a)+" -k "+str(distance)+" -w temp.txt >> resultats.txt")

with open("resultats.txt","r") as f:
    lines=f.readlines()

with open("resultats2.txt","a") as f:
    l=0
    for mot in liste_mots:
        for distance in range(1,k+1):            
            if(distance==1):
                f.write(lines[l+(distance-1)*m].strip())
            elif(distance==k):
                f.write(lines[l+(distance-1)*m].strip(mot))
            else:
                f.write((lines[l+(distance-1)*m].strip()).strip(mot))
        l+=1   
        

#os.system("rm temp.txt")
#os.system("rm resultats.txt")
#os.system("mv resultats2.txt resultats.tsv")