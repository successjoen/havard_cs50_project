#include <cs50.h>
#include <stdio.h>

// Function declarations
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate number of quarters
    int quarters = calculate_quarters(cents);
    cents -= quarters * 25;

    // Calculate number of dimes
    int dimes = calculate_dimes(cents);
    cents -= dimes * 10;

    // Calculate number of nickels
    int nickels = calculate_nickels(cents);
    cents -= nickels * 5;

    // Calculate number of pennies
    int pennies = calculate_pennies(cents);
    cents -= pennies * 1;

    // Print total coins
    int coins = quarters + dimes + nickels + pennies;
    printf("%i\n", coins);
}

int calculate_quarters(int cents)
{
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents -= 25;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = 0;
    while (cents >= 10)
    {
        dimes++;
        cents -= 10;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = 0;
    while (cents >= 5)
    {
        nickels++;
        cents -= 5;
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = 0;
    while (cents >= 1)
    {
        pennies++;
        cents -= 1;
    }
    return pennies;
}
