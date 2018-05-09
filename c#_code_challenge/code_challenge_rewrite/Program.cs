using System;

namespace code_challenge_rewrite
{
    class Program
    {
        public static void Main(string[] args)
        {
            var input = new inputClass();
            var inputString = input.getInput();

            if (input.isValid(inputString))
            {
                input.processInput(inputString);
                Console.WriteLine("**Print Tree Here**");
            }
            else
            {
                Console.WriteLine("Invalid Input");
            }

            Console.ReadLine();
        }
    }
}
