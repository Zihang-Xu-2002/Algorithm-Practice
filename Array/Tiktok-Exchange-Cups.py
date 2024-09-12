# https://www.fastprep.io/problems/tiktok-exchange-cups
from typing import List

from collections import defaultdict
class Solution(object):
    def exchangeCups(self, labels):
        numMap = defaultdict(int)
        for i, v in enumerate(labels):
            numMap[v] = i
        N = len(labels)
        count = 0
        
        for i in range(1, N):
            if numMap[i] == i - 1:
                continue
            else:
                index = numMap[i]
                
                numMap[labels[i - 1]] = index
                numMap[i] = i - 1
                labels[i - 1], labels[index] = labels[index], labels[i - 1]
                count += 1 
        return count
        
ob = Solution()
labels = [3, 1, 2, 5, 4]
print(ob.exchangeCups(labels))
