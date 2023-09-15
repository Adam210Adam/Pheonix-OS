#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

typedef enum
{
    HASHING=62,
    PRIVATE=100,
    PASSWORD=50,
    ENC_T_CF=100,
    HASHING_AND_SHORTNING=100,
    AND=100,
    OR=100,
} EncryptionMethod;

int main() {
    typedef unsigned char byte;
    typedef int bit;
    EncryptionMethod choice = PASSWORD;
    printf("Your choice is has %d%% of being secure", choice);
    scanf("");
}