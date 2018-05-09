using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace code_challenge_rewrite
{
    public class inputClass
    {
        public string getInput()
        {
            string inputString;
            Console.WriteLine("Please enter the string to process: ");
            inputString = Console.ReadLine();

            if (inputString == "")
            {
                inputString = "(id,created,employee(id,firstname,employeeType(id),lastname),location)";
            }

            return(inputString);
        }

        public bool isValid(string inputString)
        {
            if (inputString.Count(a => a == '(') != inputString.Count(b => b == ')'))
            {
                return false;
            }
            else if (inputString[0] != '(' || inputString[(inputString.Length - 1)] != ')')
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        public List<string> processInput(string inputString)
        {
            Regex search = new Regex(@"\((.+)\)");
            inputString = search.Match(inputString).Groups[1].Value;

            string[] splitResults = Regex.Split(inputString, @"([(),])");

            List<string> inputList = new List<string>();

            foreach (var s in splitResults)
            {
                if (s != "" && s != ",")
                {
                    inputList.Add(s);
                }
            }
            //Next pass the list over to the tree builder and set up the node class
            //For now, return the list
            return(inputList);
        }
    }
}
