#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double aproxima_raiz_quadrada(double A){
    if(A < 0){
        return 0;
    }
    int x = 0;
    int x0 = 1;
    while(fabs(x - x0) > 0.000001){
        x = (x0 + A/x0)/2;
        x0 = x;
    }
    return x;
}

int main(){
    printf("%lf\n", aproxima_raiz_quadrada(4));
    return 0;
}