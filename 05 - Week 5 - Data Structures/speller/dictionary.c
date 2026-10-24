#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Number of buckets in hash table (you can tweak for speed)
const unsigned int N = 10000;

// Hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

node *table[N];

// Keep track of word count
unsigned int word_count = 0;

// Hash function: djb2 (fast + good distribution)
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *word++))
    {
        c = tolower(c);
        hash = ((hash << 5) + hash) + c; // hash * 33 + c
    }

    return hash % N;
}

// Load dictionary into memory
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char buffer[LENGTH + 1];

    while (fscanf(file, "%45s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(file);
            return false;
        }

        strcpy(n->word, buffer);

        unsigned int index = hash(buffer);
        n->next = table[index];
        table[index] = n;

        word_count++;
    }

    fclose(file);
    return true;
}

// Check if word is in dictionary
bool check(const char *word)
{
    char lower[LENGTH + 1];
    int i = 0;
    for (; word[i] && i < LENGTH; i++)
    {
        lower[i] = tolower(word[i]);
    }
    lower[i] = '\0';

    unsigned int index = hash(lower);
    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(lower, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Returns number of words loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}
