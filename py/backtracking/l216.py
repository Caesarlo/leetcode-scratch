from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path = []
        self.res = []

        self.backtracking(k, n, 1)

        return self.res

    def backtracking(self, k, n, startIndex):
        if sum(self.path) > n:
            return
        if len(self.path) == k:
            if sum(self.path) == n:
                self.res.append(self.path[:])
            return

        remain = k-len(self.path)

        for i in range(startIndex, 10-remain+1):
            self.path.append(i)
            self.backtracking(k, n, i+1)
            self.path.pop()
