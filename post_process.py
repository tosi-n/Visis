from ppii import deepSpell
from ppi import word2vec_correct


def read(filename):  
    fh = open(filename, 'r')
    x = [line.split() for line in fh.read()]
    fh.close()
    return(x)

x = read("/Volumes/Loopdisk/Visis/convert.txt")

j = word2vec_correct(x)
print(j)

i = deepSpell(x, 1)
print(i)


