# Bestiary
A bestiary of analysable words

## Verif.py
Calculates the density in the neighbourhood of Levenshtein of a word taken as a parameter.

### Argument:
word whose density is calculated

### Optional arguments:
-k : Levenshtein distance (default = 4)  
-a : size of the alphabet (default = 2)  
-n : word size (default =5)  

## Classement.py :
Lists all words of size n for an alphabet of size a, calculates their density in the neighbourhood of Levenshtein using the wordborhood algorithm and orders the result into a .tsv file in order to exploit the data with spreadsheet software.

### Optional arguments:
-k : Levenshtein distance (default = 2)   
-a : size of the alphabet (default = 2)  
-n : word size (default =4)  
