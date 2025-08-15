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

    char *message = argv[1];
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