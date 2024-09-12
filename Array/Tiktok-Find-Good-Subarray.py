# https://www.fastprep.io/problems/tiktok-find-good-subarray

from typing import List
class Solution:
  def findGoodSubarrayBruteForce(self, financialMetrics: List[int], limit: int) -> int:
    goodLength = 0
    for i in range(len(financialMetrics)):
      for j in range(i+1, len(financialMetrics)):
        if min(financialMetrics[i:j]) > limit/len(financialMetrics[i:j]):
            goodLength = max(goodLength, j-i)
    return goodLength
  def findGOodSubarraySlideWindow(self, financialMetrics: List[int], limit: int) -> int:
    goodLength = -1
    for i in range(len(financialMetrics)):
      minVal = financialMetrics[i]
      for j in range(i+1, len(financialMetrics)):
        minVal = min(minVal, financialMetrics[j-1])
        if minVal > limit/len(financialMetrics[i:j]):
            goodLength = max(goodLength, j-i)
    return goodLength


solution = Solution()
financialMetrics = [1,3,4,3,1]
limit = 6
print(solution.findGOodSubarraySlideWindow(financialMetrics, limit))