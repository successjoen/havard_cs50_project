#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

// Main function
int main(int argc, string argv[])
{
    // Check for exactly two arguments (program name and key)
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    // Ensure the key is exactly 26 characters long
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }

    string key = argv[1];

    // Check all characters in the key are alphabetic
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }

        // Check for duplicate characters (case-insensitive)
        for (int j = i + 1; j < 26; j++)
        {
            if (tolower(key[i]) == tolower(key[j]))
            {
                printf("Key must not contain duplicate characters.\n");
                return 1;
            }
        }
    }

    // Get plaintext input from user
    string plain = get_string("plaintext: ");
    printf("ciphertext: ");

    // Loop through each character in the plaintext
    for (int i = 0, n = strlen(plain); i < n; i++)
    {
        char c = plain[i];

        if (isupper(c))
        {
            // Find the alphabetical index and substitute using uppercase key
            printf("%c", toupper(key[c - 'A']));
        }
        else if (islower(c))
        {
            // Find the alphabetical index and substitute using lowercase key
            printf("%c", tolower(key[c - 'a']));
        }
        else
        {
            // Leave non-alphabetic characters unchanged
            printf("%c", c);
        }
    }

    // Print newline at end
    printf("\n");
    return 0;
}
