class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                if stack == []:
                    return False
                top = stack.pop()
                if (top == '[' and i == ']') or (top == '{' and i == '}') or (top == '(' and i == ')'):
                    continue
                else:
                    return False
        return len(stack) == 0