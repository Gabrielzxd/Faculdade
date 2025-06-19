#include <stdio.h>
#include <stdbool.h>

bool forma_triangulo(double num1, double num2, double num3);

int main(){
    printf("%d\n", forma_triangulo(3,4,5));
    return 0;
}

bool forma_triangulo(double num1, double num2, double num3){
    return num1 + num2 > num3 && num1 + num3 > num2 && num2 + num3 > num1;
}