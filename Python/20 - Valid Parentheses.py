class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
             if i not in ")}]": #check i is an opening paranthesis
                 stack.append(i)
             elif stack: #If the stack is not empty
                 y = stack.pop()
                 if(y == "(" and i != ")") or (y == "{" and i != "}") or (y == "[" and i != "]"):
                     return False
             else: #if the stack is empty
                 return False

        return False if stack else True
