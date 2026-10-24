#include <stdio.h>
#include <cs50.h>

void meow(long n);

int main(void)

    // int w = 5;
    // while (w > 0)
    // {
    //     printf("meow\n");
    //     w--;
    // }

    {
        long n = get_int("number ");
        meow(1000000000000000000000000000000000000000000000);
    }


void meow(long n)
{
    for(long w = 0; w < n;w++)
    printf("meow\n");
}
