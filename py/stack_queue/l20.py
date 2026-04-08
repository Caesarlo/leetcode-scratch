class Solution:
    def isValid(self, s: str) -> bool:
        key_brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stack = []

        for i in s:
            ...
