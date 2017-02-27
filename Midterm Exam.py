"""

Midterm exam code for MIT online course Introduction to Computer Science and Programming Using Python - 6.00.1x

"""

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
    for i in L:
        if g(f(i)) == False:
            L.remove(i)
    if L == None:
        return -1
    else:
        return max(L)
    return L

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


