from typing import List
from random import randint 



def merge(a: List, l: int, m: int, r: int):
    L =[a[i] for i in range(l, m)]
    R = [a[i] for i in range(m, r)]
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0
    j = 0

    for k in range(l, r):

        if L[i] < R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

def merge_sort(a, l, r):
    if r - l > 1:
        q = (l + r)//2
        merge_sort(a, l, q)
        merge_sort(a, q, r)
        merge(a, l, q, r)




if __name__ == '__main__':
    lisa = [randint(0, 100) for j in range(40)]
    merge_sort(a=lisa, l=0, r=40)
    print(lisa)
    a = 10
    print(a)