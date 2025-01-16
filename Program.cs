
class Program
{
    
    static void Main()
    {
        Console.WriteLine("What amount of hours did you work?");
        int hours_worked = int.Parse(Console.ReadLine());
        Console.WriteLine("What amount do you make per hour you work?");
        int hourly_wages = int.Parse(Console.ReadLine());
        if (hours_worked > 40)
        {
            double PayWithOvertime = ((hourly_wages * 40) + (hourly_wages * 1.5 * (hours_worked - 40)));
            Console.WriteLine("You made this: " + PayWithOvertime);  
        }
        else
        {
            int Regular_pay = (hours_worked * hourly_wages);
            Console.WriteLine("You made this: " + Regular_pay);
        }
    }
}
