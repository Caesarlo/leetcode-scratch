from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)

        ab_map = {}

        for a in nums1:
            for b in nums2:
                ab_map[a+b] = ab_map.get(a+b, 0)+1

        count = 0

        for c in nums3:
            for d in nums4:
                if 0-(c+d) in ab_map:
                    count += ab_map[0-(c+d)]

        return count
