class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            b_set = set()

            for j in range(i+1, n):
                if j > i+2 and nums[j] == nums[j-1] and nums[j-1] == nums[j-2]:
                    continue

                target = 0-(nums[i]+nums[j])

                if target in b_set:
                    res.append([nums[i], target, nums[j]])
                    b_set.remove(target)
                else:
                    b_set.add(nums[j])

        return res
