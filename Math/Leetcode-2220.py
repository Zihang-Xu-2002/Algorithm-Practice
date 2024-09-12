class Solution:
    def getBinary(self, num):
        result = []
        while num > 0:
            result.append(num%2)
            num = num//2
        return result
    def minBitFlips(self, start: int, goal: int) -> int:
        startBinary = self.getBinary(start)
        print(startBinary)
        goalBinary = self.getBinary(goal)
        print(goalBinary)

        change = 0
        if len(startBinary) < len(goalBinary):
            tmp = [0]*(len(goalBinary)-len(startBinary))
            startBinary += tmp
        else:
            tmp = [0]*(len(startBinary)-len(goalBinary))
            goalBinary += tmp
        for i in range(len(startBinary)):
            if startBinary[i] != goalBinary[i]:
                change += 1
        return change