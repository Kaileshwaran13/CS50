#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main(){
    int value[] = {1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
    char player1[100];
    printf("Player 1: ");
    scanf("%[^\n]%*c", player1);
    char player2[100];
    printf("Player 2: ");
    scanf("%[^\n]%*c", player2);
    int count1 = 0,count2 = 0;
    for(int i = 0; i < strlen(player1); i++){
        if(isalpha(player1[i])){
            if(islower(player1[i])){
                count1 += value[player1[i] - 'a'];
            }
            else
            {
                count1 += value[player1[i] - 'A'];
            }
        }
    }
    for(int i = 0; i < strlen(player2); i++){
        if(isalpha(player2[i])){
            if(islower(player2[i])){
                count2 += value[player2[i] - 'a'];
            }
            else
            {
                count2 += value[player2[i] - 'A'];
            }
        }
    }
    if(count1 > count2){
        printf("Player 1 wins!\n");
    }
    else if(count1 < count2){
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

}