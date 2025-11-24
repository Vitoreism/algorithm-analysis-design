#include<stdio.h>

#define TAM 10

void selection_sort(int a[], int n){
    int i_min, aux;
    for(int i = 0; i < n-1; i++){
        i_min = i;

        for(int j = i+1; j < n; j++){
            if(a[j] < a[i_min]){
                i_min = j;
            }
        }
        if(i != i_min){
            aux = a[i_min];
            a[i_min] = a[i];
            a[i] = aux;
        }
    }
}

void print_array(int a[], int n){
    for(int i = 0; i < n; i++){
        printf("%d\n", a[i]);
    }
}


int main(void){
    int array[TAM] = {3, 5, 10, 1, 2, 7, 4, 6, 9, 8};
    print_array(array, TAM);
    selection_sort(array, TAM);
    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    print_array(array, TAM);
}