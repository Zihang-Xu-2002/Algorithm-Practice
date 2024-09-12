# https://www.fastprep.io/problems/tiktok-card-packets
from typing import List
class Solution:
  def cardPackets(self, cardTypes: List[int]) -> int:
    
    packsRange = max(cardTypes)
    sumAdd = float('inf')
    if packsRange == 1:
        return 2*len(cardTypes)-sum(cardTypes)
    if packsRange == 0:
        return 2*len(cardTypes)
    for packs in range(2, packsRange+1):
        tmp = 0
        for i in range(len(cardTypes)):
            val = cardTypes[i] % packs
            if val > 0:
                tmp += (packs - val)
        sumAdd = min(sumAdd, tmp)
    return sumAdd
  
# Test case
testCase = [[4, 7, 5, 11, 15],[3, 8, 7, 6, 4],[3, 9, 7, 6, 5, 2],[1,1,1,1,1]]
solution = Solution()
for item in testCase:
    print(solution.cardPackets(item))