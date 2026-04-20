from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for i in nums:
            count_map[i] = count_map.get(i, 0)+1

        pq = []

        for num, freq in count_map.items():
            heapq.heappush(pq, (freq, num))
            if len(pq) > k:
                heapq.heappop(pq)

        return [num for freq, num in pq]
