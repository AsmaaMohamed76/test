#include<stdio.h>
#include<stdlib.h>

int main()
{
    double num1;
    double num2;
    double num3;
    double sum;
    printf("Enter Your First Number: ");
    scanf("%lf", &num1);
    printf("Enter Your Second Number: ");
    scanf("%lf", &num2);
     printf("Enter Your Third Number: ");
    scanf("%lf", &num3);
    sum = num1 + num2 + num3;
    printf("The Result of Summation is : %f\n", sum);
    printf("The Average is : %f",sum/3);
    return 0;
    
}