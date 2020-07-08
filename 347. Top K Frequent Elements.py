#-*- coding:utf-8 -*-
#@Date   : 2018/11/23
#@Author : suyifan
#@File   : 347. Top K Frequent Elements.py




nums = [1,1,1,2,2,4,4,4,5,4]
k = 2


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        counts = collections.Counter(nums)
        import heapq as hq
        # dict1 = {}
        # for i in nums:
        #     dict1[i] = dict1.get(i,0) + 1
        # print(dict1,"---")
        heap = []
        for key,value in counts.items():
            hq.heappush(heap,(value,key))
            if len(heap) > k:
                hq.heappop(heap)
        ans = []
        for _ in range(k):
            ans.append(hq.heappop(heap)[1])
        return ans[::-1]
# class Solution:
#     def topKFrequent(self, nums, k):
#         import collections
#         import heapq
#         counts = collections.Counter(nums)
#         print(nums)
#         heap = []
#         for num, count in counts.items():
#             heapq.heappush(heap, (count, num))
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         res = []
#         for _ in range(k):
#             res.append(heapq.heappop(heap)[1])
#         return res[::-1]

a = Solution()
q = a.topKFrequent(nums,k)
print("q =",q)