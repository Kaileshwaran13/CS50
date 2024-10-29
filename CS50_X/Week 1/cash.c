#include<stdio.h>

int main()
{
    int num = -1;
    while(num < 0){
        printf("Change owed: ");
        scanf("%d",&num);
    }
    int change = 0;
    if(num >= 25)
    {
        change += num / 25;
        num %= 25;
    }
    if(num >= 10)
    {
        change += num / 10;
        num %= 10;
    }
    if(num >= 5)
    {
        change += num / 5;
        num %= 5;
    }
    if(num >= 1)
    {
        change += num / 1;
        num %= 1;
    }
    printf("%d",change);
}