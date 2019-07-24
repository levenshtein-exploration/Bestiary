import os
from itertools import product, repeat
from editdistance import eval as dist

k=5 #distance
a=2 #taille de l'alphabet
n=5 #taille des mots

liste=[]

for taille in range (n-k,n+k+1):
    iteration=product("ab",repeat=taille)
    for element in iteration:
        if(dist(str(element).replace("', '","").strip("('')").strip("',"),"babba")<=k):
            liste.append(str(element).replace("', '","").strip("('')").strip("',"))

print(len(liste))       
        
        




