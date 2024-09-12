# https://www.fastprep.io/problems/tiktok-find-minimum-transitions
from typing import List
class Solution:

    def minTransitions(self,arr: List[int]) -> int:
        n = len(arr)
        m = sum(arr)
        k = sum(arr[:m])
        return min(m-k, k)
        


# Test case
test_arr = [1, 0, 1, 0, 1]
solution = Solution()

print(solution.minTransitions(test_arr)) # 0
    