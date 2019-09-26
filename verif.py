import os
import argparse
from itertools import product, repeat
from editdistance import eval as dist

parser = argparse.ArgumentParser()
# parser.add_argument("-a", type=int, default=2) #distance
# parser.add_argument("-n", type=int, default=5) #alphabet size
# parser.add_argument("-k", type=int, default=4) #word size
parser.add_argument("-a", type=int, default=2)
parser.add_argument("-k", type=int, default=4)
parser.add_argument("word", type=str) #the word whose density is calculated in the neighbourhood of Levenshtein
args = parser.parse_args()

def main():
    k=args.k
    a=args.a
    word=args.word
    n = len(word)
    liste=[]
    alphabet=""
    #create the alphabet used 
    for letter in list(map(chr, range(ord("a"), ord("a")+a))):
        alphabet+=letter
    #lists all possible words from size n-k to n+k
    for size in range (n-k,n+k+1):
        iteration=product(alphabet,repeat=size)
        #keep only the words with a distance <=k
        for element in iteration:
            generated = "".join(element)
            if(dist(generated,word)<=k):
                liste.append(generated)
    print(len(liste))

if __name__== "__main__":
  main()