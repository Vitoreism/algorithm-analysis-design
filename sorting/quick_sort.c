#include<stdio.h>

#define TAM 10

int partition(int a[], int l, int r){
    int pivot = a[l]; // Escolhendo o primeiro elemento do vetor como sendo o pivo
    int i = l - 1;
    int j = r + 1;
    int aux; 

    while(1){
        do{
            i++;
        }while(a[i] < pivot);
        
        do{ 
            j--;
        }while(a[j] > pivot);
        
        if(i >= j){
            return j;
        }

        aux = a[i];
        a[i] = a[j];
        a[j] = aux;
    }
}

void quickSort(int a[], int l, int r){
    if(l < r){
        int q = partition(a, l, r);
        quickSort(a, l, q);
        quickSort(a, q+1, r);
    }
}

void print_array(int a[], int n){
    for(int i = 0; i < n; i++){
        printf("%d\n", a[i]);
    }
}


int main(void){
    int array[TAM] = {3, 5, 10, 1, 2, 7, 4, 6, 9, 8};
    quickSort(array, 0, TAM-1);
    print_array(array, TAM);
}