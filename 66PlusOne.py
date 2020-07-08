#-*- coding:utf-8 -*-
#@Date   : 2018/9/4
#@Author : huali
#@File   : 66PlusOne.py


digits = [9,9,9]

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # if digits == [9]:
        #     return [1,0]

        count = 0
        digits[-1] += 1

        for i in range(len(digits)-1,0,-1):
            # print("---")
            if digits[i] > 9 :
                digits[i] = 0
                digits[i-1] +=1
                count += 1
            else:
                break
            if count == 0 :
                digits[i] += 1
                break

        # if digits[0] >9 :
        #     digits.append("a")
        #     for i in range(1,len(digits)):
        #         digits[i] = 0
        #     digits[0] =1

        if digits[0] > 9 :
            digits.append(0)
            digits[0] = 1


        return digits

a = Solution()
q = a.plusOne(digits)
print("q=",q)