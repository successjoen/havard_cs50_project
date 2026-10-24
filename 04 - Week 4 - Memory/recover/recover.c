#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Size of each block to read from memory card
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure proper usage: expect exactly one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card file
    FILE *card = fopen(argv[1], "r");

    // Check if the file could not be opened
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Create a buffer to store data blocks
    uint8_t buffer[BLOCK_SIZE];

    // Variables for output JPEG file
    FILE *img = NULL;
    char filename[8];
    int counter = 0;

    // Read blocks of 512 bytes until end of file
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Check for JPEG signature at the start of the block
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
           (buffer[3] & 0xf0) == 0xe0)
        {
            // If already writing a JPEG, close it
            if (img != NULL)
            {
                fclose(img);
            }

            // Create a new JPEG file
            sprintf(filename, "%03i.jpg", counter);
            img = fopen(filename, "w");

            // Increment counter for next image
            counter++;
        }

        // If a JPEG file is open, write the block to it
        if (img != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, img);
        }
    }

    // Close any remaining open files
    if (img != NULL)
    {
        fclose(img);
    }

    fclose(card);
    return 0;
}

