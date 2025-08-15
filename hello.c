#include <stdio.h>
#include <string.h>
#include <windows.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Usage: ./hello word1 word2 word3 ...");
        return 1;
    }

    char combined[4096] = "";

    for (int i = 1; i < argc; i++)
    {
        strcat(combined, argv[i]);
        if (i < argc - 1)
        {
            strcat(combined, " ");
        }
    }

    char *message = combined;
    int len = strlen(message);

    char output_msg[len + 1];
    output_msg[len] = '\0';

    for (int i = 0; i <= len; i++)
    {
        char msg_char = message[i];

        for (int j = 0, targ = msg_char; j <= targ; j++)
        {
            output_msg[i] = (char) j;
            output_msg[i + 1] = '\0';
            printf("%s\n", output_msg);
            Sleep(1);
        }
    }
}