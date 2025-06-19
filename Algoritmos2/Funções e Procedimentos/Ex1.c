#include <stdio.h>

int maior_valor(int num1, int num2, int num3);

int main(){
    int num = maior_valor(4,5,6);
    printf("%d\n", num);
    return 0;
}

int maior_valor(int num1, int num2, int num3){
    int maior = num1;
    if (num2 > maior) maior = num2;
    if (num3 > maior) maior = num3;
    return maior;
}