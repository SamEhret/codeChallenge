using System;

namespace code_challenge_rewrite
{
    public class inputClass
    {
        public void getInput()
        {
            string inputString;
            Console.WriteLine("Please enter the string to process: ");
            inputString = Console.ReadLine();

            if (inputString == "")
            {
                inputString = "(id,created,employee(id,firstname,employeeType(id),lastname),location)";
            }
            Console.WriteLine(inputString);
        }
    }
}
