using System;
using System.Collections.Generic;

namespace code_challenge_rewrite
{
    public class BuildTree
    {
        public Node BuildNodes(List<string> inputList)
        {
            var root = new Node("");
            var tempRoot = root;
            foreach (string item in inputList)
            {
                if (item == "(")
                {
                    tempRoot = tempRoot.children[(tempRoot.children.Count - 1)];
                }
                else if (item == ")")
                {
                    tempRoot = tempRoot.parent;
                }
                else
                {
                    tempRoot.children.Add(new Node(item));
                    tempRoot.children[(tempRoot.children.Count - 1)].parent = tempRoot;
                }
            }
            return root;
        }
    }
}
