# calcul.py

"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `combinaison(x1, x2)` - Returns the number of combination.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

from math import *


def combinaison(x1, x2) :
    """Check the calculs result of combination

    Args:
        x1 (float): series of dice 1
        x2 (float): series of dice 2

    Returns:
        Result (int): number of combination
    """
    p = 1 / 6
    if (x1 == 0) :
        result = binomial(x2, x2)
    elif (x2 == 0) :
        result = binomial(x1, x1)
    else :
        coef = factorial(x1 + x2) / (factorial(x1) * factorial(x2))
        result = coef * (p ** (x1 + x2))
    return result

def binomial(n, k) :
    """Return a calcul of the binomial

    Args:
        n (float): n éléments
        k (float): combinaison de k parmi n

    Returns:
        Result (int): number of combination with binomial
    """
    p = 1 / 6
    coef = factorial(n) / (factorial(k) * factorial(n - k))
    result = coef * pow(p, k) * pow(1 - p, n - k)
    return result

def pair(occ, throw) :
    """Compute and return the probability of have a brelan

    Args:
        occ (float): list all the occurence
        throw (float): nombre de lancer

    Returns:
        Percentage (float): Percentage for have a four of kind
    """
    i = 0
    count = 0
    result = 0.00

    while (len(throw) != i) :
        if (occ == int(throw[i])) :
            count = count + 1
        i = i + 1
    if (count >= 2) :
        result = 100.00
        print("Chances to get a ", occ, " pair: ", "%.2f" % (result), "%", sep='')
    else :
        i = 1
        while (i != 6) :
            if (i + count >= 2 and i + count <= 5) :
                result = result + binomial(5 - count, i)
            i = i + 1
        print("Chances to get a ", occ, " pair: ", "%.2f" % (result * 100), "%", sep='')

def brelan(occ, throw) :
    """Compute and return the probability of have a brelan

    Args:
        occ (float): list all the occurence
        throw (float): nombre de lancer

    Returns:
        Percentage (float): Percentage for have a brelan
    """
    i = 0
    count = 0
    result = 1.00

    while (len(throw) != i) :
        if (occ == int(throw[i])) :
            count = count + 1
        i = i + 1
    if (count >= 3) :
       result = 100.00
       print("Chances to get a ", occ, " three-of-a-kind: ", "%.2f" % (result), "%", sep='')
    else :
        i = 1
        while (i != 6) :
            if (i + count >= 3 and i + count <= 5) :
                result = result + binomial(5 - count, i)
            i = i + 1
        print("Chances to get a ", occ, " three-of-a-kind: ", "%.2f" % (result), "%", sep='')

def carre(occ, throw) :
    """Compute and return the probability of have a four of kind
    
    Args: 
        occ: All the occurence result
        throw: Number of throws

    Returns:
        Percentage (float): Percentage for have a four of kind
    """
    i = 0
    count = 0
    result = 0.00

    while (len(throw) != i) :
        if (occ == int(throw[i])) :
            count = count + 1
        i = i + 1
    if (count >= 4) :
       result = 100.00
       print("Chances to get a ", occ, " four-of-a-kind: ", "%.2f" % (result), "%", sep='')
    else :
        i = 1
        while (i != 6) :
            if (i + count >= 4 and i + count <= 5) :
                result = result + binomial(5 - count, i)
            i = i + 1
        print("Chances to get a ", occ, " four-of-a-kind: ", "%.2f" % (result * 100), "%", sep='')

def full(occ3, occ2, throw) :
    """Compute and return the probability of have a full
    
    Args: 
        occ3: The first occurence you want
        occ2: The second occurence you want
        throw: Number of throws

    Returns:
        Percentage (float): Percentage for have a full
    """
    i = 0
    count3 = 0
    count2 = 0
    result = 0.00

    while (len(throw) != i) :
        if (occ3 == int(throw[i])) :
            count3 = count3 + 1
        if (occ2 == int(throw[i])) :
            count2 = count2 + 1
        i = i + 1
    if (count3 == 3 and count2 == 2) :
        result = 100.00
        print("Chances to get a ", occ3, " full of ", occ2, ": %.2f" % (result), "%", sep='')
    else :
        result = combinaison(3 - count3, 2 - count2)
        print("Chances to get a ", occ3, " full of ", occ2, ": %.2f" % (result * 100), "%", sep='')

def straight(occ, throw) :
    """Compute and return the probability of have a straight
    
    Args: 
    occ: All the occurence result
    throw: Number of throws

    Returns:
        Percentage (float): Percentage for have a straight
    """
    save = occ
    i = 0
    same_dice = 0
    count = 0
    result = 0.00

    occ = 1
    while (occ != 7) :
        while (len(throw) != i) :
            if (occ == int(throw[i])) :
                same_dice = same_dice + 1
            i = i + 1
        occ = occ + 1
        if (same_dice == 0) :
            count = count + 1
        same_dice = 0
        i = 0
    print(count)
    if (count == 100) :
        result = 100.00
        print("Chances to get a ", save, " straight: ", "%.2f" % (result), "%", sep='')
    else :
        result = 1 / (6 ** (count - 1)) * 100
        print("Chances to get a ", save, " straight: ", "%.2f" % (result), "%", sep='')

def yahtzee(occ, throw) :
    """Compute and return the probability of have a yahtzee
    
    Args: 
    occ: All the occurence result
    throw: Number of throws

    Returns:
        Percentage (float): Percentage for have a yahtzee
    """
    i = 0
    count = 0
    result = 1.00

    while (len(throw) != i) :
        if (occ == int(throw[i])) :
            count = count + 1
        i = i + 1
    if (count >= 5) :
       result = 100.00
       print("Chances to get a ", occ, " yams: ", "%.2f" % (result), "%", sep='')
    else :
        result = 1 / (6 ** (5 - count)) * 100
        print("Chances to get a ", occ, " yams: ", "%.2f" % (result), "%", sep='')
help(combinaison)
help(binomial)
help(pair)
help(brelan)
help(yahtzee)
help(carre)
