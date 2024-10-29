// Basic Calculator

#include<stdio.h>

int addDigits(int num1,int num2){
    return (float)(num1+num2);
}
int subDigits(int num1,int num2){
    return (float)(num1-num2);
}
int mulDigits(int num1,int num2){
    return (float)(num1*num2);
}
int divDigits(int num1,int num2){
    return (float)(num1/num2);
}

int main(){
    printf("Basic Calculator to the arithmetic operations +,-,*,/ \n");
    int num1 = 0, num2 = 0;
    char oper;
    printf("Num1 = ");
    scanf("%d",&num1);
    printf("Num2 = ");
    scanf("%d",&num2);
    printf("Operator = ");
    scanf(" %c",&oper);
    printf("Givn Equation: %d %c %d\n",num1,oper,num2);
    float ans = 0;
    switch(oper){
        case '+':
            ans = addDigits(num1,num2);
            break;
        case '-':
            ans = subDigits(num1,num2);
            break;
        case '*':
            ans = mulDigits(num1,num2);
            break;
        case '/':
            ans = divDigits(num1,num2);
            break;
    }
    printf("Answer of \" %d %c %d = %.2f\"\n",num1,oper,num2,ans);
    return 0;
}


