from typing import List
from random import randint

def counting_sort(a: List[int], b: List[int],k: int, n: int) -> List[int]:
    ...
    # Primeiro passo no counting sort é criar o vetor auxiliar de contagem -> Ele deve ter k + 1 elementos
    # Esse vetor deve ser inicializado com 0
    c = [0 for i in range(k+1)]

    # Depois, devemos preencher o vetor com as contagens dos elementos
    for i in range(n):
        c[a[i]] += 1
    
    # Em seguida, devemos implementar a pare de guarda as frequencias acumulativas
    for i in range(1, len(c)):
        c[i] += c[i-1]
    
    # Iterar da direita pra esquerda pelo vetor A (Garante a estabilidade)
    for i in range(n-1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]

    return b
def find_max(a: List[int]):
    _max = 0

    for i in range(len(a)):
        if a[i] > _max:
            _max = a[i]
    
    return _max 


if __name__ == '__main__':
    lista = [randint(1, 50) for i in range(30)]
    print(lista)
    k = find_max(lista)
    lista_ordenada = counting_sort(a=lista, b=[0 for i in range(len(lista))], k=k, n=len(lista))
    print(lista_ordenada)