#-*- coding:utf-8 -*-
#@Date   : 2019/7/18
#@Author : huali
#@File   : 1078. Occurrences After Bigram.py


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        list1 = text.split()

        is_first = False
        ans = []
        n = len(list1)
        for i, word in enumerate(list1):
            if word == first:
                is_first = True
            if is_first:
                if word == second and i < n - 1:
                    ans.append(list1[i + 1])
                if word != first:
                    is_first = False
        return ans
a =Solution()
q = a.findOcurrences(text,first,second)
print(f"q={q}")