using System;

// Command prompt - dotnet new console
//                  dotnet run
namespace _9_CSharp
{
    class Magic8Ball
    {
        /*
            These are the possible answers to the Magic8Ball. Very
            much like was done in Python, but note that we have to
            declare the type of thing we want.
        */
        static string [] answers = new string[] {
                "Ask again later",
                "Outlook is good",
                "Yes",
                "No",
                "Most likely no",
                "Most likely yes",
                "Maybe",
                "Outlook is not good"
            };
        static void Main(string[] args)
        {
            // Random number generator (in System)
            Random rand = new Random();

            // Variable to hold the user response
            string current_answer = null;
            do
            {
                // Clear the console
                Console.Clear();

                // As for a question
                Console.WriteLine("What would you like to ask?");
                current_answer = Console.ReadLine();

                // If the answer is q then quit
                if(current_answer.ToLower() == "q")
                    break;

                // Get the index into the array
                int next_answer = rand.Next(0,Magic8Ball.answers.Length - 1);

                // Print out the question and answer
                Console.WriteLine(String.Format("You asked : {0}",current_answer));
                Console.WriteLine(String.Format("Magic 8 Ball says : {0}",Magic8Ball.answers[next_answer]));

                // Because we clear, have them hit enter
                Console.WriteLine("\nPress the enter key to continue...");
                Console.ReadLine();

            }while(true);

        }
    }
}
