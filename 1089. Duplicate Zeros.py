#-*- coding:utf-8 -*-
#@Date   : 2019/7/12
#@Author : huali
#@File   : 1089. Duplicate Zeros.py


"""
给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

 

示例 1：

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：

输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
 

提示：

1 <= arr.length <= 10000
0 <= arr[i] <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/duplicate-zeros
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

arr = [1,0,2,3,0,4,5,0]
# 暴力法
# class Solution:
#     def duplicateZeros(self, arr: "List[int]") -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         n = len(arr)
#         i = 0
#         while i < n:
#             num = arr[i]
#             if num == 0 and i < n-1:
#                 for j in range(n-1,i+1,-1):
#                     arr[j] = arr[j-1]
#                 arr[i+1] = 0
#                 i += 1
#             i += 1



        # print(arr)
        # return arr

# a = Solution()
# q = a.duplicateZeros(arr)
# print(f"q={q}")



# -------------------------双指针,从后往前复制----------------
arr = [1,0,2,3,0,4,5,0]
arr = [8,4,5,0,0,0,0,7]
class Solution:
    def duplicateZeros(self, arr: "List[int]") -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        k = n

        for i,num in enumerate(arr):
            if i < k - 1:
                if num == 0:
                    k -= 1
            else:
                break
        print(k,"sdfa")
        right = k
        n -= 1
        while right >= 0:
            if arr[right] == 0:
                arr[n] = 0
                n -= 1
            arr[n] = arr[right]
            n -= 1
            right -= 1

        print(arr)
        # return arr

a = Solution()
q = a.duplicateZeros(arr)
# print(f"q={q}")