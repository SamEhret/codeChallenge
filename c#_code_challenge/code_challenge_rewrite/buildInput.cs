using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text.RegularExpressions;

namespace code_challenge_rewrite
{
    public static class InputClass
    {
        public static string GetInput()
        {
            Console.WriteLine("Please enter the string to process: ");
            var inputString = Console.ReadLine();

            if (inputString == "")
            {
                inputString = "(id,created,employee(id,firstname,employeeType(id),lastname),location)";
            }

            return(inputString);
        }

        public static bool IsValid(string inputString)
        {   
            if (inputString.Count(a => a == '(') != inputString.Count(b => b == ')'))
            {
                return false;
            }

            if (inputString[0] != '(' || inputString[(inputString.Length - 1)] != ')')
            {
                return false;
            }
            
            return true;
        }

        public static IEnumerable<string> ProcessInput(string inputString)
        {
            var search = new Regex(@"\((.+)\)");
            inputString = search.Match(inputString).Groups[1].Value;

            var splitResults = Regex.Split(inputString, @"([(),])");

            var inputList = splitResults.Where(s => s != "" && s != ",").ToList();

            return(inputList);
        }
    }
}