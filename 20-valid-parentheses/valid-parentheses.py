class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
                continue
            
            if ( (stack[-1] == "(" and char == ")") or 
            (stack[-1] == "{" and char == "}") or 
            (stack[-1] == "[" and char == "]") ):
                stack.pop()
                continue
            
            stack.append(char)
        return not stack
