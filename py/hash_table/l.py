from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n_dict = defaultdict()

        for i in range(len(nums)):
            if nums[i] in n_dict and abs(n_dict[nums[i]]-i) <= k:
                return True

            n_dict[nums[i]] = i

        return False
