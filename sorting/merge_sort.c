#include<stdio.h>

#include<math.h>



#define INF 100000

#define TAM 10





void merge(int a[], int l,int m, int r){
    int L[(m-l)+1], R[(r-m)+1];

    for(int i = 0; i < (m-l); i++){
        L[i] = a[l+i];
    }

    for(int i = 0; i < (r-m); i++){
        R[i] = a[m+i];
    }

    L[m-l] = INF;
    R[r-m] = INF;
    
    int i = 0, j = 0;

    for(int k = l; k < r; k++){
        if(L[i] < R[j]){
            a[k] = L[i];
            i++;
        }
        else{
            a[k] = R[j];
            j++;
        }
    }
}





void merge_sort(int a[], int l, int r){
    int q;
    if(r - l> 1){
        q = (l+r)/2;
        merge_sort(a, l, q);
        merge_sort(a, q, r);
        merge(a, l, q, r);
    }
}



void print_array(int a[], int n){
    for(int i = 0; i < n; i++){
        printf("%d\n", a[i]);
    }

}





int main(void){
    int a[TAM] = {5, 3 ,1, 7, 6, 2, 4, 10, 8 ,9};
    merge_sort(a, 0, TAM);
    print_array(a, TAM);

}