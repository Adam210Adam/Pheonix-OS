#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main() {
    int BL, BX;
    BL = 0b0000;
    BX = 0b0000;
    int AL = BX & BL;

    printf("InfoNUM: %d", AL);
    return EXIT_SUCCESS;
}