/*
Relação de Recorrência
qnt_chamadas_0 = 1
qnt_chamadas_1 = 1
qnt_chamadas_n = qnt_chamadas_n-1 + qnt_chamadas_n-2 + 1
*/

#include <stdio.h>

int qnt_chamadas(int n){
    if(n < 0){
        return -999;
    } else{
        if(n == 0 || n == 1){
            return 1;
        } else{
            return qnt_chamadas(n-1) + qnt_chamadas(n-2) + 1;
        }
    }
}