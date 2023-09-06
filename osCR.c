#include <stdio.h>
#include <stdint.h>
#include <Bootloader.h>
#include <stdlib.h>
#include <windows.h>

int main()
{
    boot(0); // Boot from the Bootloader.h Header file
    // Holds The Debugging console from exiting
    MessageBeep(MB_OKCANCEL);
    int HolderForCconsole;
    printf("Press Enter To exit the program... \n");
    scanf("*%d", &HolderForCconsole);

    return EXIT_SUCCESS;
}