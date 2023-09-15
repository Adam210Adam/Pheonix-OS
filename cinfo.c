#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main() {
    uint8_t uint8Max = UINT8_MAX;
    uint16_t uint16Max = UINT16_MAX;
    uint32_t uint32Max = UINT32_MAX;
    uint64_t uint64Max = UINT64_MAX;
    printf("%12u | UINT8_MAX\n", uint8Max);
    printf("%12u | UINT16_MAX\n", uint16Max);
    printf("%12u | UINT32_MAX\n", uint32Max);
    printf("%12u | UINT64_MAX\n", uint64Max);
    unsigned int holder;
    scanf("%u", holder);
}