#-*- coding:utf-8 -*-
#@Date   : 2018/11/29
#@Author : suyifan
#@File   : 239. Sliding Window Maximum.py



nums = [1,3,-1,-3,5,3,6,7]
k = 3

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        ans = []
        heap = nums[:k-1]
        for num in nums[k-1:]:

            heap.append(num)
            max_num = max(heap)  # 这里用最大堆实现,时间复杂度log k
                                    # ,因为k是常数所以可以认为是线性
                                    #python 里面没有最大堆,只有最小堆
                                #所以就这么写凑合了

            ans.append(max_num)
            heap.pop(0)
        return ans

a = Solution()
q = a.maxSlidingWindow(nums,k)
print("q =",q)