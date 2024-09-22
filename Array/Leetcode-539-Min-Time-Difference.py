class Solution:
    def getTimeDiff(self, t1, t2):
        # t1 和 t2 是以分钟为单位的时间点，计算时间差
        return min(abs(t2 - t1), 1440 - abs(t2 - t1))

    def findMinDifference(self, timePoints: List[str]) -> int:
        # 将时间转换为分钟表示
        timePointsNum = []
        for i in timePoints:
            hours, mins = i.split(":")
            total_minutes = int(hours) * 60 + int(mins)
            timePointsNum.append(total_minutes)
        
        # 对时间点进行排序
        timePointsNum.sort()

        # 初始化最小时间差为一个很大的数
        min_diff = float('inf')

        # 比较相邻时间点的差值
        for i in range(1, len(timePointsNum)):
            min_diff = min(min_diff, self.getTimeDiff(timePointsNum[i-1], timePointsNum[i]))

        # 还需要比较最后一个时间点和第一个时间点跨越午夜的情况
        min_diff = min(min_diff, self.getTimeDiff(timePointsNum[0], timePointsNum[-1]))

        return min_diff


        
