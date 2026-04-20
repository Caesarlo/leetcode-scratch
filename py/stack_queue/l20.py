class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        bracket_map = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for i in s:
            if i in bracket_map:
                stack.append(bracket_map[i])
                continue
            else:
                if not stack or i != stack[-1]:
                    return False
                stack.pop()

        return not stack
