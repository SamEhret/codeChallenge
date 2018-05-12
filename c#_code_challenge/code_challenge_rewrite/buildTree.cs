using System;
using System.Collections.Generic;

namespace code_challenge_rewrite
{
    public static class BuildTree
    {
        public static Node BuildNodes(IEnumerable<string> inputList)
        {
            var root = new Node("");
            var tempRoot = root;
            foreach (var item in inputList)
            {
                switch (item)
                {
                    case "(":
                        tempRoot = tempRoot.children[(tempRoot.children.Count - 1)];
                        break;
                    case ")":
                        tempRoot = tempRoot.parent;
                        break;
                    default:
                        tempRoot.children.Add(new Node(item));
                        tempRoot.children[(tempRoot.children.Count - 1)].parent = tempRoot;
                        break;
                }
            }
            return root;
        }
    }
}