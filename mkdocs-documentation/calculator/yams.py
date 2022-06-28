#!/usr/bin/env python3

import sys
from calcul import *

def search_func():
    nbr = int(str_list[1])
    if (str_list[0] == "pair"):
        pair(nbr, nbr_list)
    elif (str_list[0] == "full"):
        if (len(str_list) != 3 or str_list[1] == str_list[2]):
            sys.exit(84)
        full(nbr, int(str_list[2]),nbr_list)
    elif (str_list[0] == "four"):
        carre(nbr, nbr_list)
    elif (str_list[0] == "straight"):
        straight(nbr, nbr_list)
    elif (str_list[0] == "yams"):
        yahtzee(nbr, nbr_list)
    elif (str_list[0] == "three"):
        brelan(nbr, nbr_list)

if (len(sys.argv) == 2
 and sys.argv[1] == "-h"):
    print("USAGE\n    ./201yams d1 d2 d3 d4 d5 c\n\nDESCRIPTION\n   d1      value of the first die (0 if not throw)")
    print("   d2      value of the first die (0 if not throw)")
    print("   d3      value of the first die (0 if not throw)")
    print("   d4      value of the first die (0 if not throw)")
    print("   d5      value of the first die (0 if not throw)")
    print("   c       expected combinaison")
    sys.exit(84)

if (len(sys.argv) < 7):
    print ("We need to have 5 number equal one face of dice and what do you want\nnot enough arg")
    sys.exit(84)

if (len(sys.argv) > 7):
    print ("We need to have 5 number equal one face of dice and what do you want\ntoo many arg")
    sys.exit(84)


nbr_list = list()

nbr_list.append(sys.argv[1])
nbr_list.append(sys.argv[2])
nbr_list.append(sys.argv[3])
nbr_list.append(sys.argv[4])
nbr_list.append(sys.argv[5])
txt = sys.argv[6]
str_list = txt.split("_")

i = 0;

while  (i != len(nbr_list) and nbr_list[i].isnumeric() == True  and int(nbr_list[i]) <= 6 and int(nbr_list[i]) >= 0):
    i = i + 1

if (i != len(nbr_list) and nbr_list[i].isnumeric() == False):
    print("We need to have: this sentence figure_number and number is between 1 and 6")
    sys.exit(84)

if (i != len(nbr_list) and (int(nbr_list[i]) > 6 or int(nbr_list[i]) < 0)):
    print("We need to have: this sentence figure_number and number is between 1 and 6")
    sys.exit(84)

i = 1

while  (i != len(str_list) and str_list[i].isnumeric() == True  and int(str_list[i]) <= 6 and int(str_list[i]) >= 0):
    i = i + 1

if (i != len(str_list) and str_list[i].isnumeric() == False):
    print("We need to have: this sentence figure_number and number is between 1 and 6")
    sys.exit(84)

if (i != len(str_list) and (int(str_list[i]) > 6 or int(str_list[i]) < 0)):
    print("We need to have: this sentence figure_number and number is between 1 and 6")
    sys.exit(84)


if (len(str_list) != 2 and len(str_list) != 3 or str_list[1].isnumeric() == False or int(str_list[1]) > 6 or int(str_list[1]) <= 0):
    print("We need to have: this sentence figure_number and number is between 1 and 6")
    sys.exit(84)

if (str_list[0] == "pair" or str_list[0] == "full" or str_list[0] == "four" or str_list[0] == "straight" or str_list[0] == "yams" or str_list[0] == "three"):
    search_func()
    sys.exit(0)
else :
    print("Wrong name for figure")
    sys.exit(84)
