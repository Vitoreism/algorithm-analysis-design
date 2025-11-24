from typing import List, Union

def selection_sort(a: List[Union[int, float]], n: int) -> List[Union[int, float]]:

    for i in range(n-1):
        i_min  = i

        for j in range(i+1, n):

            if a[j] < a[i_min]:
                i_min = j    
        
        if i_min != i:
            aux = a[i_min]
            a[i_min] = a[i]
            a[i] = aux 
    
    return a

if __name__ == '__main__':
    array = [5, 2, 7, 10, 4, 3, 6, 9, 8, 1]

    print(selection_sort(array, len(array)))