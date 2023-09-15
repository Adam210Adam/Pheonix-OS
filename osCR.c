#include <stdio.h>
#include <stdint.h>
#include <Bootloader.h>
#include <stdlib.h>
#include <windows.h>
#include <unistd.h>
#include <stdbool.h>

int main()
{
    typedef unsigned char byte;
    typedef int bit;
    typedef unsigned Uint;
    boot(0); // Boot from the Bootloader.h Header file
    // Holds The Debugging console from exiting
    MessageBeep(MB_OKCANCEL);
    int HolderForCconsole;
    printf("Press Any Key And press enter To exit the operating system...");
    scanf("%d", &HolderForCconsole);

    return EXIT_SUCCESS;
}