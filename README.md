# Bestiary
A bestiary of analysable words

## verif.py
Calculates the density in the neighbourhood of Levenshtein of a word taken as a parameter.
This is not optimal because it's an enumeration of all words.
This script was create to verify the output of wordborhood.

### Argument:
The word to compute the neighborhood density

### Optional arguments:
* k : Levenshtein distance (default = 4)
* a : size of the alphabet (default = 2)

## classement.py :
Lists all words of size n for an alphabet of size a.
Then calculates their density regarding the Levenshtein neighbourhood using the wordborhood algorithm.
The results are sorted into a .tsv file.

### Optional arguments:
-k : Levenshtein distance (default = 2)   
-a : size of the alphabet (default = 2)  
-n : word size (default =4)  
