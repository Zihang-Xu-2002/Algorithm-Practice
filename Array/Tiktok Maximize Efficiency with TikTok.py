from typing import List

class Solution:
  def maximizeEfficiencyProduct(self, efficiencyScores: List[int]) -> int:
    sortedScores = sorted(efficiencyScores)
    maxFiveScores = sortedScores[-5:]
    result = 1
    for i in maxFiveScores:
      result *= i
    return result
    # 还要考虑有负数的情况！