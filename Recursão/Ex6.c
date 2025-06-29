#define flag -1
#include <stdio.h>

int function(int a, int b){
    if(a < 0 || b % 10 != b){
        return flag;
    } else{
        if(a == 0){
            return 0;
        } else{
            if(a % 10 == b){
                return 1 + function(a / 10, b);
            } else{
                return function(a / 10, b);
            }
        }
    }
}

int main() {
    int resultado = function(5253552, 5);  // Espera: 3
    printf("Resultado: %d\n", resultado);
    return 0;
}
