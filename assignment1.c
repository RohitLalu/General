#include <stdio.h>

//user defined functions
int power(unsigned int a, int pow);
int sop(int a, int b);

//global var
int num=0;

//main 
int main(int n,char* argvs)
{
    num = n;
    unsigned int a,b;
    int result;
    printf("Enter a: ");
    scanf("%u",&a); // intentional bug
    printf("\nEnter b: ");
    scanf("%u",&b);
    result = sop(a,b);
    printf("Final result: %d",result);
    return 0;
}

int power(unsigned int a, int pow){
    int prod=1;
    for (int i=0;i<pow;i++){
        prod*=a;
    }
    return prod;
}

int sop(int a, int b){
    int sum;
    sum = power(a,num)+power(b,num);
    return sum;
}

