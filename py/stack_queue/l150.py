from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 2:
            return int(tokens[0])

        stack = []
        res = 0

        operators = ['+', '-', '*', '/']

        for item in tokens:
            if item in operators and len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                if item == '+':
                    stack.append(a+b)
                if item == '-':
                    stack.append(a-b)
                if item == '*':
                    stack.append(a*b)
                if item == '/':
                    stack.append(int(a/b))
            else:
                stack.append(item)

        return stack[0]
