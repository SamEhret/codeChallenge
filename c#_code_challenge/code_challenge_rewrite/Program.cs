using System;

namespace code_challenge_rewrite
{
    class Program
    {
        public static void Main(string[] args)
        {
            var Input = new InputClass();
            var BuildTree = new BuildTree();

            var inputString = Input.GetInput();

            if (Input.IsValid(inputString))
            {
                var inputList = Input.ProcessInput(inputString);
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
