#include<stdio.h>

int main(){
    int num;
    printf("Height : ");
    scanf("%d",&num);
    while(num <= 0){
        printf("Height : ");
        scanf("%d",&num);
    }
    for (int i = 1; i <= num; i++){
        for(int j = num-i; j > 0 ;j--){
            printf(" ");
        }
        for(int j = 0; j < i; j++){
            printf("#");
        }
        printf("\n");
    }
}