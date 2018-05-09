using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

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

            isValid(inputString);
        }

        public void isValid(string inputString)
        {
            if (inputString.Count(a => a == '(') != inputString.Count(b => b == ')'))
            {
                Console.WriteLine("Invalid Input");
            }

            else if (inputString[0] != '(' || inputString[(inputString.Length - 1)] != ')')
            {
                Console.WriteLine("Invalid Input");
            }

            else
            {
                processInput(inputString);
            }
        }

        public void processInput(string inputString)
        {
            Regex search = new Regex(@"\((.+)\)");
            inputString = search.Match(inputString).Groups[1].Value;

            string[] splitResults = Regex.Split(inputString, @"([(),])");

            List<string> newList = new List<string>();

            foreach (var s in splitResults)
            {
                if (s != "" && s != ",")
                {
                    newList.Add(s);
                }
            }
            //Next pass the list over to the tree builder and set up the node class
        }
    }
}
