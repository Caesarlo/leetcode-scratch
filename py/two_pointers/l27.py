from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
                count += 1

        return count
