#include<stdio.h>

#define SIZE 10

void print_array(int a[], int size){
    for(int i = 0; i < size; i++){
        printf("%d ", a[i]);
    }
}

void bubble_sort(int a[], int size){
    int swap = 1, aux;
    while(swap){
        swap = 0;
        for(int i = 0; i < size-1; i++){
            if (a[i] > a[i+1]){
                aux = a[i];
                a[i] = a[i+1];
                a[i+1] = aux;
                swap = 1;
            }
        }
    }
}



int main(void){
    int array[] = {7, 5, 6,3, 2, 9, 5, 7, 6, 1};
    print_array(array, SIZE);
    printf("\n\n");
    bubble_sort(array, SIZE);
    print_array(array, SIZE);
}   