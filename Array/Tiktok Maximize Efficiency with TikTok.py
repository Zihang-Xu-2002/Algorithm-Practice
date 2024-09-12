from typing import List

class Solution:
    def maximizeEfficiencyProduct(self, efficiencyScores: List[int]) -> int:
        # 对数组进行排序
        sortedScores = sorted(efficiencyScores)
        
        # 第一种情况：选择5个最大的数
        maxFiveScores = sortedScores[-5:]
        result1 = 1
        for i in maxFiveScores:
            result1 *= i
        
        # 第二种情况：选择两个最小的负数和三个最大的正数
        result2 = float('-inf')
        if len(sortedScores) >= 5:
            result2 = sortedScores[0] * sortedScores[1] * sortedScores[-1] * sortedScores[-2] * sortedScores[-3]
        
        # 第三种情况：选择四个最小的负数和一个最大的正数
        result3 = float('-inf')
        if len(sortedScores) >= 5:
            result3 = sortedScores[0] * sortedScores[1] * sortedScores[2] * sortedScores[3] * sortedScores[-1]

        # 返回三种方案中的最大值
        return max(result1, result2, result3)