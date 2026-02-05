from typing import List, Union
from random import randint

def bubble_sort(a: List[Union[int, float]]) -> None:
    swap = True
    while swap:
        swap = False
        for i in range(len(a) - 1):
            if a[i ] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                swap = True 
    


if __name__ == '__main__':
    size_list = randint(15, 100)
    print(f"Size of the list: {size_list}")
    test_list = [randint(0, 100) for i in range(size_list)]

    print(f"Test list: {test_list}")
    bubble_sort(test_list)
    print(f"Sorted list: {test_list}")