#include <stdio.h>

int main (void) {
    char frase[255];
    scanf("%s", frase);
    printf("----\n");
    int i;
    for (i=1; i<5; i++) {
        printf("%d %s\n", i, frase);
    }
    printf("----\n");
    return 0;
}
