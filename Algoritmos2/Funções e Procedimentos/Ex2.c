#include <stdio.h>

void imprime_divisores(int num1, int num2, int num3);

int main(){
    imprime_divisores(4,6,2);
    return 0;
}

void imprime_divisores(int num1, int num2, int num3){
    if(num3 != 0){
        if(num1 >= num2){
            for(int i = num2; i <= num1; i++){
                if(i % num3 == 0){
                    printf("%d \n", i);
                }
            }
        } else{
            for(int i = num2; i >= num1; i--){
                if(i % num3 == 0){
                    printf("%d \n", i);
                }
            }
        }
    }
}
