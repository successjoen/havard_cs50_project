#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // code to loop height if above 8 and below 1
    int height;
    do
    {
        height = get_int("height");
    }
    while (height < 1 || height > 8);

    int e, h;
    // code for the left side of the pyramid
    for (h = 0; h < height; h++)
    {
        // code for the space that made the pyramid to face right
        for (e = height - 1; e > h; e--)
        {
            {
                printf(" ");
            }
        }

        for (e = 0; e < h + 1; e++)
        {
            {
                printf("#");
            }
        }
        printf("  ");

        // code for right pyramid

        for (e = 0; e < h + 1; e++)
        {
            {
                printf("#");
            }
        }
        printf("\n");
    }
}
