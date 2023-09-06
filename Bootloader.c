#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <windows.h>

void clearScreen()
{
    const char *CLEAR_SCREEN_ANSI = "\e[1;1H\e[2J";
    write(STDOUT_FILENO, CLEAR_SCREEN_ANSI, 12);
}
int boot(int x) {
    printf("Booting From CPU Sector 0xaa 0x55\n\n\n\n");
    printf("Choose A operating System To Boot From:\n\n\n");
    printf("Pheonix OS\n");
    int Submition;
    scanf("%d", Submition);
    printf("\n");
    clearScreen();
    printf("C: ");
    char command[100];
    scanf("%d", &command);
}