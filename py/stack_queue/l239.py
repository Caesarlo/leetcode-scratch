
from typing import List
from collections import deque


class Solution:
    """
    超时了
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        queue = deque()
        res = []
        for i in range(k-1):
            queue.append(nums[i])

        for i in range(len(nums)-k+1):
            queue.append(nums[i+k-1])
            res .append(max(queue))
            queue.popleft()

        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []

        for i in range(len(nums)):
            if queue and queue[0] < i-k+1:
                queue.popleft()

            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

            queue.append(i)

            if i >= k-1:
                res.append(nums[queue[0]])

        return res
