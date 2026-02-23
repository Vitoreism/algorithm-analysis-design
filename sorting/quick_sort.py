from typing import List, Union
from random import randint


def partition(a: List[Union[int, float]], l: int, r: int):
    """
    a -> Array de valores numéricos 
    l -> endereço de memória do primeiro elemento do array
    r -> endereço de memória do último elemento do array
    """
    pivot = a[l] # Implementando com o pivo sendo o primeiro elemento do vetor 
    i = l - 1 
    j = r + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1 
        
        j -= 1
        while a[j] > pivot:
            j -= 1
        
        if i >= j:
            return j 

        # Swap
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
    

def quickSort(a, l, r):
    if l < r:
        q = partition(a, l, r)
        quickSort(a, l, q)
        quickSort(a, q+1, r)


if __name__ == '__main__':
    size_list = randint(50, 150)
    print(f"Tamanho da lista: {size_list}")
    numeros = [randint(1, 100) for i in range(size_list)]
    quickSort(numeros, 0, size_list-1)
    print(numeros)