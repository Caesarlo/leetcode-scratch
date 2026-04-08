class Solution0:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp_str = s+s

        temp_str = temp_str[1:-1]

        return True if s in temp_str else False


class Solution:

    def getNext(self, s: str):
        next = [0]*len(s)
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1

            next[i] = j

        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False

        next = self.getNext(s)

        length = len(s)

        if next[length-1] != 0 and length % (length-(next[length-1])) == 0:
            return True

        return False
