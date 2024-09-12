# https://www.fastprep.io/problems/tiktok-eating-candies

from typing import List
class Solution:
  def mostCandiesEaten(self, candies: List[int]) -> int:
    if len(candies) <= 1:
      return 0
    aEat = 0
    bEat = 0
    possibleEat = 0
    a = 0
    b = len(candies) - 1
    while  a < b:
      if aEat < bEat:
        aEat += candies[a]
        a += 1
      else:
        bEat += candies[b]
        b -= 1
      if aEat == bEat:
        possibleEat = max(possibleEat, aEat)

    return possibleEat

# Test case
testCase = [[1000],[1,2,1]]
solution = Solution()
for item in testCase:
    print(solution.mostCandiesEaten(item)) 
      
      
    