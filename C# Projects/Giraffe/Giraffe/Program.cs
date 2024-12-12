// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
// prompts a number to the user
Console.WriteLine("enter a number to check: ");
// reads the number and makes it a variable
int oechecker = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("the number is: "+ oechecker);

// checks to see the modulas of the numebr to test if even or odd
if (oechecker %2 == 0)
{
    Console.WriteLine("The number is even");
}
else
{
    Console.WriteLine("The number is odd");
}