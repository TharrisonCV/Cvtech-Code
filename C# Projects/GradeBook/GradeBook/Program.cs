using System;

class Program
{
    //gathers data for string values
    static string dataStrGather()
    {
        Console.WriteLine("Enter your first Name: ");
        string Fn = Console.ReadLine();
        Console.WriteLine("Enter your last Name: ");
        string Ln = Console.ReadLine();
        string FullName = Fn + " " + Ln;

        return FullName;
    }
    //gathers data for int
    static (int, int, int) dataIntGather()
    {
        Console.WriteLine("Enter 1st Grade: ");
        int G1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter 2nd Grade: ");
        int G2 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Enter 3rd Grade: ");
        int G3 = Convert.ToInt32(Console.ReadLine());

        return (G1, G2, G3);
    }

    //calc avrager
    static int calcAvg(int G1, int G2, int G3)
    {
        int average = (G1 + G2 + G3) / 3;
        return average;
    }

    //determines letter grades
    static string letterGrade(int average)
    {
        if (average >= 90)
        {
            return "A";
        }
        else if (average >= 80)
        {
            return "B";
        }
        else if (average >= 70)
        {
            return "C";
        }
        else if (average >= 60)
        {
            return "D";
        }
        else
        {
            return "F";
        }

    }

    //dispalys data
    static void displayData(string gradeLetter, int average, string FullName)
    {
        Console.WriteLine("Your grade level is "+ gradeLetter);
        Console.WriteLine("Your Average is " + average);
        Console.WriteLine("Your name is " + FullName);
    }

    //calls all functions 
    static void Main()
    {
        string fullName = dataStrGather();

        var (g1,g2,g3) = dataIntGather();
        int average = calcAvg(g1, g2, g3);
        string gradeLetter = letterGrade(average);
        displayData(gradeLetter, average, fullName);
    }
}
