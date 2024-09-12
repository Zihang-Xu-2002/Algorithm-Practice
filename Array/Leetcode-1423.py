from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefix1 = []
        sum1 = 0
        for i in range(len(cardPoints)):
            sum1 += cardPoints[i]
            prefix1.append(sum1)
        sum2 = 0
        prefix2 = []
        for i in range(len(cardPoints)-1, -1, -1):
            sum2 += cardPoints[i]
            prefix2.append(sum2)
        maxVal = prefix2[k-1]
        for i in range(k+1):
            num1 = i
            num2 = k-i
            if (num1-1)>=0 and (num2-1)>=0:
                maxVal = max(maxVal, prefix1[num1-1]+prefix2[num2-1])
            elif num1-1<0:
                maxVal = max(maxVal, prefix2[num2-1])
            elif num2-1<0:
                maxVal = max(maxVal, prefix1[num1-1])
        return maxVal