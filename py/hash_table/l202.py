class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n != 1:
            if n in res:
                return False
            res.add(n)
            n = self.cal(n)

        return True

    def cal(self, n: int) -> int:
        res = 0
        while n > 0:
            temp = n % 10
            res += temp**2
            n //= 10
        return res


class Solution1:
    def isHappy(self, n: int) -> bool:
        res = set()
        while n != 1:
            if n in res:
                return False
            res.add(n)
            n = self.cal(n)

        return True

    def cal(self, n: int) -> int:
        res = 0
        while n:
            n, r = divmod(n, 10)
            res += r**2
        return res
