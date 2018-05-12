using System;

namespace code_challenge_rewrite
{
    internal static class Program
    {
        public static void Main(string[] args)
        {
            var inputString = InputClass.GetInput();

            if (InputClass.IsValid(inputString))
            {
                var inputList = InputClass.ProcessInput(inputString);
                var printString = BuildTree.BuildNodes(inputList);
                Console.WriteLine(printString.ToString());
            }
            else
            {
                Console.WriteLine("Invalid Input");
            }

            Console.ReadLine();
        }
    }
}