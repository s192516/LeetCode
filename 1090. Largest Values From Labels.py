#-*- coding:utf-8 -*-
#@Date   : 2019/7/12
#@Author : huali
#@File   : 1090. Largest Values From Labels.py

'''
我们有一个项的集合，其中第 i 项的值为 values[i]，标签为 labels[i]。

我们从这些项中选出一个子集 S，这样一来：

|S| <= num_wanted
对于任意的标签 L，子集 S 中标签为 L 的项的数目总满足 <= use_limit。
返回子集 S 的最大可能的 和。

 

示例 1：

输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。
示例 2：

输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。
示例 3：

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
输出：16
解释：选出的子集是第一项和第四项。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-values-from-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 1

class Solution:
    def largestValsFromLabels(self, values: "List[int]", labels: "List[int]", num_wanted: int, use_limit: int) -> int:

        import collections
        dict1 = collections.defaultdict(list)
        for i,l in enumerate(labels):
            dict1[l].append(values[i])

        list1 = []
        for k,v in dict1.items():
            n = len(v)
            if n > use_limit:
                list1.extend(sorted(v,reverse= True)[:use_limit])
            else:
                list1.extend(v)

        n = min(num_wanted,len(list1))
        ans = sum(sorted(list1,reverse=True)[:n])
        return ans


a = Solution()
q = a.largestValsFromLabels(values,labels,num_wanted,use_limit)
print(f"q={q}")