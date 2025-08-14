#include <stdio.h>
#include <string.h>
#include <windows.h>

char MESSAGE[] = "Hello World!";

int main(void)
{
    int len = strlen(MESSAGE);

    char output_msg[len + 1];
    output_msg[len] = '\0';

    for (int i = 0; i <= len; i++)
    {
        char msg_char = MESSAGE[i];

        for (int j = 0, targ = msg_char; j <= targ; j++)
        {
            output_msg[i] = (char) j;
            output_msg[i + 1] = '\0';
            printf("%s\n", output_msg);
            Sleep(1);
        }
    }
}