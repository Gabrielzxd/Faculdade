#include <stdio.h>

int MDC(int a, int b){
    if(a < 0 || b < 0){
        return -999;
    } else{
        if(b == 0){
            return a;
        } else{
            return MDC(a, a % b);
        }
    }
}