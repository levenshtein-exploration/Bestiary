import os
import argparse
import string
from subprocess import run, PIPE
from itertools import product, repeat

#Manages arguments:
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", type=int, default=2) #alphabet size
    parser.add_argument("-n", type=int, default=4) #word size
    parser.add_argument("-k", type=int, default=2) #distance
    args = parser.parse_args() 
    return args

#Creates a list of all words of size n for an alphabet of size a, write the list to a text file "temp.txt" and return the list:
def temp_maker(a, n):
    alphabet=""
    list_mots=[]
    for letter in list(map(chr, range(ord("a"), ord("a")+a))):
        alphabet+=letter
    iteration=product(alphabet,repeat=n)    
    for element in iteration:
        list_mots.append(str(element).replace("', '","").strip("('')"))
    with open("temp.txt","a") as f:
        for mot in list_mots:
            f.write(mot+"\n")
    return list_mots

#Calls the wordborhood program for each word and each k and formats the output into a "results.tsv" file:
def output_maker(a, k, n, list_mots):
    m=pow(a,n) #number of words
    for distance in range(1,k+1):
        result=run(["./wordborhood","-d","dula"+str(distance)+".fsm","-a",str(a),"-k",str(distance),"-w","temp.txt"],stdout=PIPE,text=True)
        with open("resultats.txt","a") as f:
            f.write(result.stdout)
    with open("resultats.txt","r") as f:
        lines=f.readlines()
    with open("resultats2.txt","a") as f:
        l=0
        for mot in list_mots:
            for distance in range(1,k+1):            
                if(distance==1):
                    f.write(lines[l+(distance-1)*m].strip())
                elif(distance==k):
                    f.write(lines[l+(distance-1)*m].strip(mot))
                else:
                    f.write((lines[l+(distance-1)*m].strip()).strip(mot))
            l+=1
    os.system("rm temp.txt")
    os.system("rm resultats.txt")
    os.system("mv resultats2.txt resultats.tsv")

   

def main():
    args=parse_arguments()
    k=args.k #distance
    a=args.a #taille de l'alphabet
    n=args.n #taille des mots    
    output_maker(a, k, n, temp_maker(a, n))
    
if __name__== "__main__":
  main()