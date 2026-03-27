class Solution0:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        res = dict()

        for i in s:
            if i not in res:
                res[i] = 1
            else:
                res[i] += 1

        for i in t:
            if i not in res:
                res[i] = 1
            else:
                res[i] -= 1

        for k in res:
            if res[k] != 0:
                return False
            else:
                res[k] = 1

        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in s:
            count[i] = count.get(i, 0)+1

        for i in t:
            if i not in count:
                return False
            count[i] -= 1
            if count[i] < 0:
                return False

        return True
