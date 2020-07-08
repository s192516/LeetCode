#-*- coding:utf-8 -*-
#@Date   : 2019/7/11
#@Author : huali
#@File   : 1093. Statistics from a Large Sample.py

'''
我们对 0 到 255 之间的整数进行采样，并将结果存储在数组 count 中：count[k] 就是整数 k 的采样个数。

我们以 浮点数 数组的形式，分别返回样本的最小值、最大值、平均值、中位数和众数。其中，众数是保证唯一的。

我们先来回顾一下中位数的知识：

如果样本中的元素有序，并且元素数量为奇数时，中位数为最中间的那个元素；
如果样本中的元素有序，并且元素数量为偶数时，中位数为中间的两个元素的平均值。
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/statistics-from-a-large-sample
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



'''

count = [1,2,3,3,3,6,7]
# 小,大,平均,中位,众数
class Solution:
    def sampleStats(self, count: "List[int]") -> 'List[float]':
        ans = []

        min_num = 999
        max_num = -1
        sum_all = 0
        n = 0
        zhongshu = -1
        zhongshu_count = -1
        for i,num in enumerate(count):
            if num != 0:
                min_num = min(i,min_num)
                max_num = max(i,max_num)
                sum_all += i * num
                n += num
                if num > zhongshu_count:
                    zhongshu_count = num
                    zhongshu = i

                # zhongshu = max(zhongshu,num)

        idx = 0

        if n % 2 == 0:
            list1 = [n//2,n//2+1]
        else:
            list1 = [n//2+1,n//2+1]

        for i,num in enumerate(count):
            if idx + num >= list1[1]:
                zhongweishu = i
                break
            elif idx + num == list1[0]:
                if n % 2 != 0:
                    zhongweishu = i
                else:
                    for j in range(i+1,256):
                        if count[i]:
                            zhongweishu = (i+j)/2
                            break
                break
            idx += num
        ans.append(min_num)
        ans.append(max_num)
        ans.append(sum_all/n)
        ans.append(zhongweishu)
        ans.append(zhongshu)


        return ans

a = Solution()
q = a.sampleStats(count)
print(f"q = {q}")







