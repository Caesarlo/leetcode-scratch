class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = list(s.split())

        if len(pattern) != len(s):
            return False

        p_to_s = {}
        s_to_p = {}

        for i in range(len(pattern)):
            a = pattern[i]
            b = s[i]

            if a in p_to_s and p_to_s[a] != b:
                return False

            if b in s_to_p and s_to_p[b] != a:
                return False

            p_to_s[a] = b
            s_to_p[b] = a

        return True
