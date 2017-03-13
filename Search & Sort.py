def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

def search3(L, e):
    print("List L: " + str(L))
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

def bubble_sort(L):
    swap = False
    while not swap:
        print(L)
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                tmp = L[j]
                L[j] = L[j-1]
                L[j-1] = tmp
                swap = False

def sel_sort(L):
    index = 0
    while index != len(L):
        print(L)
        for i in range(index+1, len(L)):
            if L[i] < L[index]:
                L[index], L[i] = L[i], L[index]
        index += 1

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

