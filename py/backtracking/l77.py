from typing import List


class Solution0:

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(n, k, 1)

        return self.res

    def backtracking(self, n, k, startIndex):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return

        for i in range(startIndex, n+1):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(n, k, 1)

        return self.res

    def backtracking(self, n, k, startIndex):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return

        for i in range(startIndex, n-(k-len(self.path))+2):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
