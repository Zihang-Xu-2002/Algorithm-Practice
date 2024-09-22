import math
from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def canReduceToZero(workerTimes, mountainHeight, T):
            totalReduction = 0
            for workerTime in workerTimes:
                # Solve for maximum x such that workerTime * (x * (x + 1)) / 2 <= T
                maxX = int((-1 + math.sqrt(1 + 8 * T / workerTime)) // 2)
                totalReduction += maxX
                if totalReduction >= mountainHeight:
                    return True
            return totalReduction >= mountainHeight

        low, high = 1, (1 + mountainHeight) * mountainHeight * max(workerTimes) // 2

        while low < high:
            mid = (low + high) // 2
            if canReduceToZero(workerTimes, mountainHeight, mid):
                high = mid  # Try for a smaller time
            else:
                low = mid + 1  # Increase the time
        return int(low)
