#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isNumeric(const char *str)
{
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (!isdigit((unsigned char) str[i]))
        {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    if (argc == 2 && isNumeric(argv[1]))
    {
        int num = atoi(argv[1]);
        while (num > 26)
        {
            num = num - 26;
        }
        if (num > 0)
        {
            char text[1000];
            printf("plaintext: ");
            scanf(" %[^\n]s", text);
            char cipher[1000] = "";
            unsigned char ans;
            for (int i = 0; i < strlen(text); i++)
            {
                ans = (unsigned char) text[i] + num;
                if (islower(text[i]) && ans > 'z')
                {
                    cipher[i] = 'a' + (ans - 'z' - 1);
                }
                else if (isupper(text[i]) && ans > 'Z')
                {
                    cipher[i] = 'A' + (ans - 'Z' - 1);
                }
                else
                {
                    if (isalpha(text[i]))
                    {
                        cipher[i] = ans;
                    }
                    else
                    {
                        cipher[i] = text[i];
                    }
                }
            }
            printf("ciphertext: %s\n", cipher);
        }
        else
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    return 0;
}
