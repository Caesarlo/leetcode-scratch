from typing import List


class Solution0:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for h in range(len(citations)):
            if citations[h] < h+1:
                return h
        return len(citations)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)

        for i, c in enumerate(citations):
            if c < i+1:
                return i

        return len(citations)
