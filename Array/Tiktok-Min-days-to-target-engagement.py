# https://www.fastprep.io/problems/tiktok-min-days-to-target-engagement
from typing import List
def minDaysToTargetEngagement(initialScore: int, targetScore: int, trainingScore: List[int]) -> int:
    dayCounter = 1
    
    while initialScore < targetScore:
      if initialScore < min(trainingScore):
        initialScore += dayCounter
        dayCounter += 1
        continue
      else:
        tmp = []
        toRemove = 0
        for i in trainingScore:
          if initialScore >= i and i > dayCounter:
            tmp.append(i)
        if tmp == []:
          initialScore += dayCounter
        else:
            toRemove = max(tmp)
            initialScore += toRemove
            trainingScore.remove(toRemove)
        dayCounter += 1
        continue
    return dayCounter-1

initial = 0
target = 30
training = [15,3,2]
print(minDaysToTargetEngagement(initial, target, training)) # 