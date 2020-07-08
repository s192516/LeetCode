#-*- coding:utf-8 -*-
#@Date   : 2019/1/4
#@Author : suyifan
#@File   : 539. Minimum Time Difference.py

timePoints = ["23:59","00:00"]
timePoints = ["23:59","07:00","08:00"]
# timePoints = ["07:00","07:06"]
# timePoints = ["00:00","23:59","00:00"]
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # n = len(timePoints)
        self.t = timePoints
        # max1 = 720
        # min1 = 720
        ans = 720
        set_time = set(timePoints)
        if len(set_time) != len(timePoints):
            return 0
        for time in set_time:
            ans = min(self.plus(time, ans), ans)
            ans = min(self.jian(time, ans), ans)

        return ans

    def jian(self,time,ans):
        hour = int(time[:2])
        minute = int(time[3:])
        for i in range(1, ans):
            if minute == 0:
                minute = 59
                if hour == 0:
                    hour = 23
                else:
                    hour -= 1
            else:
                minute -= 1

            m1, h1 = False, False
            if minute < 10:
                minute = "0" + str(minute)
                m1 = True
            if hour < 10:
                hour = "0" + str(hour)
                h1 = True
            now = str(hour) + ":" + str(minute)
            if now in self.t:
                return i
            if m1 :
                minute = int(minute)
            if h1 :
                hour = int(hour)
        return ans


    def plus(self, time, max1):
        hour = int(time[:2])
        minute = int(time[3:])
        for i in range(1, max1):
            if minute == 59:
                minute = 0
                if hour == 23:
                    hour = 0
                else:
                    hour += 1
            else:
                minute += 1

            m1,h1 = False,False
            if minute < 10:
                minute = "0"+str(minute)
                m1 = True
            if hour < 10:
                hour = "0"+str(hour)
                h1 = True
            now = str(hour) + ":" + str(minute)
            if now in self.t:
                return i
            if m1 :
                minute = int(minute)
            if h1 :
                hour = int(hour)


        return max1

a = Solution()
q = a.findMinDifference(timePoints)
print("q =",q)
