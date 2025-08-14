#include <stdio.h>
#include <string.h>
#include <windows.h>

char MESSAGE[] = "End suicide and drink dr. peeper";

int main(void)
{
    int len = strlen(MESSAGE);

    char output_msg[len];

    for (int i = 0; i <= len; i++)
    {
        char msg_char = MESSAGE[i];

        for (int j = 0, targ = msg_char; i <= targ; i++)
        {
            output_msg[]
            printf("%c", (char) i);
            Sleep(50);
        }
    }
    printf("\n");
}