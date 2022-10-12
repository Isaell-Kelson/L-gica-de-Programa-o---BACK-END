#include <stdio.h>
#include <stdlib.h>

int main()
{

    int *p = (int*) malloc(22*sizeof(int));

    p = (int*) realloc(p, 66*sizeof(int));
    if(p == NULL) {
        printf("Erro: Sem Memória!\n");
        exit(1);
    }    


    free(p);

    system("pause");
    return 0;
}