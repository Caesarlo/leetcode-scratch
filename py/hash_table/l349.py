from typing import List


class Solution0:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}

        for i in nums1:
            count[i] = count.get(i, 0)+1

        res = []

        for i in nums2:
            if i in count and i not in res:
                res.append(i)

        return res


class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        nums1 = set(nums1)

        for i in nums2:
            if i in nums1 and i not in res:
                res.add(i)

        return list(res)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
