from typing import List


class Solution0:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i]-cost[i]
            total += diff
            tank += diff

            if tank < 0:
                tank = 0
                start = i+1

        return start if total >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        spare = 0
        minSpare = float('inf')
        minIndex = 0

        for i in range(len(gas)):
            spare += gas[i]-cost[i]
            if spare < minSpare:
                minSpare = spare
                minIndex = i

        return (minIndex+1) % len(gas) if spare >= 0 else -1
