using System;
using System.Collections.Generic;

namespace code_challenge_rewrite
{
    public class Node
    {
        public string name;
        public Node parent;
        public List<Node> children;

        public Node(string value)
        {
            name = value;
            parent = null;
            children = new List<Node>();
        }

        public string ToString(int level = -1)
        {
            string printString = "";
            for (int i = 0; i < level; i++)
            {
                printString = $"{new String('-', level)}";
            }
            printString += $"{name}\n";

            children.Sort((a, b) => (a.name.CompareTo(b.name)));

            foreach (var child in children)
            {
                printString += child.ToString(level + 1);
            }
            return printString;
        }
    }
}