from typing import List, Union
def insertion_sort(a: List[Union[int, float]], n: int) -> List[Union[int, float]]:
    
    for i in range(1, n):
        pivot = a[i]
        j = i - 1

        while j >= 0 and a[j] > pivot: 
            a[j+1] = a[j]
            j -= 1
        
        a[j+1] = pivot 
    
    return a












def insertion_sort2(a: List[Union[int, float]], n: int) -> List[Union[int, float]]:

    for i in range(1, n):

        pivot = a[i]
        j = i - 1

        while j>= 0 and a[j] > pivot:
            a[j+1] = a[j]
            j -= 1
        
        a[j+1] = pivot 
    
    return a 






















if __name__ == '__main__':
    array = [1, 5, 2, 10, 2, 3, 4, 7, 9]
    print(insertion_sort2(a=array, n=len(array)))