"""

Midterm exam code for MIT online course Introduction to Computer Science and Programming Using Python - 6.00.1x

"""

"""
#1-1： False
#1-2： False
#1-3： False
#1-4： False
#1-5： False
#1-6： True
#1-7： False
#1-8： False
#1-9： True
#1-10：True

#2-1：L has integer keys
#2-2: The loop will always immediately terminate.
#2-3: a tuple 
#2-4: type(s) can be tuple
#2-5: for i in range(1000001, -1, -2): print(f)


#3-1: ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
[ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
["iQ"]

#3-2: Python has arbitrary precision arithmetic.

#4: See below function defintion

#5: See below function defintion
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    i = 0 
    while base ** i < num:
        i += 1
    if ((base ** i) - num) >= (num - (base ** (i - 1))):
        return i - 1
    else:
        return i

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    num = 0
    for i in range(len(listA)):
        num += (listA[i] * listB[i])
    return num

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(len(L)):
        if type(L[i]) == list:
            L[i].reverse()
    return L.reverse()

def dict_interdiff(d1, d2):
    """
    The function takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries:
    a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

    intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2.
    To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values
    -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function.
    Do not implement f inside your dict_interdiff code -- assume it is defined outside.

    difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.

    :param d1: dictionary
    :param d2: dictionary
    :return t: a tuple of two dictionaries
    """
    d3 = {}
    d4 = {}
    t = (d3, d4)
    for key in (set(d1).union(set(d2))):
        if key in (set(d1).intersection(set(d2))):
            d3.update({key: f(d1[key], d2[key])})
        else:
            if key in d1.keys():
                d4.update({key: d1[key]})
            else:
                d4.update({key: d2[key]})
    return t

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    list_remove = []
    for i in L:
        if not g(f(i)):
            list_remove.append(i)
    else:
        for i in list_remove:
            L.remove(i)
        if L == []:
            return -1
        return max(L)


def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    fList=[]
    for element in aList:
        if type(element) == list:
            fList.extend(flatten(element))
        else:
            fList.append(element)
    return fList


