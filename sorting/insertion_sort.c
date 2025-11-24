#include<stdio.h>

#define TAM 10


void insertion_sort(int a[], int n){
    int pivot, j;

    for(int i = 1; i < n; i++){
        pivot = a[i];
        j = i - 1;

        while(j >= 0 && a[j] > pivot){
            a[j+1] = a[j];
            j--;
        }
        a[j + 1] = pivot;
    }

}

void print_array(int a[], int n){
    for(int i = 0; i < n; i++){
        printf("%d\n", a[i]);
    }
}


int main(void){
    int a[TAM] = {5, 3 ,1, 7, 6, 2, 4, 10, 8 ,9};
    int pivot, j;
    print_array(a, TAM);
    insertion_sort(a, TAM);
    printf("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n");
    print_array(a, TAM);

}