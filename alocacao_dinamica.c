#include <stdio.h>

int main()
{
    int *ponteiro_para_inteiro;                                                       /* Cria um ponteiro para uma variável inteira  */
    int tamanho;                                                                      /* Salva o tamanho digitado pelo usuário       */
    
    ponteiro_para_inteiro = malloc(22 * sizeof(int));                                 /* Aloca 22 espaços de memória para o ponteiro */

    if(!ponteiro_para_inteiro)                                                        /* Verifica se a memória foi alocada, e se     */
    {                                                                                 /* não for possível alocar, sai do programa    */
        printf("Erro ao alocar memoria!\n");
        return 1;
    }
    printf("Vetor de tamanho 22 criado com sucesso!\n");

    printf("Digite um novo tamanho de vetor:\n");
    scanf("%d", &tamanho);
    ponteiro_para_inteiro = realloc(ponteiro_para_inteiro, tamanho * sizeof(int));    /* Realoca mais ou menos memória               */
    if(!ponteiro_para_inteiro)                                                        /* Nova verificação de alocação                */
    {
        printf("Erro ao alocar memoria!\n");
        return 1;
    }
    printf("Vetor realocado com tamanho %d!\n", tamanho);
    system("pause");

    free(ponteiro_para_inteiro);                                                      /* Libera a memória para o heap                */
}