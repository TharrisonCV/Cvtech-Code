// See https://aka.ms/new-console-template for more information
using System.Security.Cryptography;
Random random = new Random();
Console.WriteLine("Welcome to Guessing Game!");


// generates random number
int randomNumber = random.Next(1, 101);
// prompts a number to the user
Console.WriteLine("enter a number to check (Between 1-100): ");
// reads the number and makes it a variable
int guesschecker = Convert.ToInt32(Console.ReadLine());
while (guesschecker != randomNumber)
{
    // checks if the guess is higher than random number
    if (guesschecker > randomNumber)
    {
        Console.WriteLine("You guessed it incorrectly, try to guess lower.");
    }
    // checks if guess is lower than the random number
    else if (guesschecker < randomNumber)
    {
        Console.WriteLine("You guessed it incorrectly, try to guess higher.");
    }
    else
    {
        Console.WriteLine("Nan");
    }
    // prompts a number to the user
    Console.WriteLine("enter a number to check: ");
    // reads the number and makes it a variable
    guesschecker = Convert.ToInt32(Console.ReadLine());
}
//ending statment to print the random number
Console.WriteLine("correct the number was: " + randomNumber);