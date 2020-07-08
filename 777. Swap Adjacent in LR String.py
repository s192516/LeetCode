#-*- coding:utf-8 -*-
#@Date   : 2018/9/13
#@Author : suyifan
#@File   : 777. Swap Adjacent in LR String.py



##### 总之,start的R可以一直向右移动直到碰到L,L可以一直向左移动,直到碰到R
##### 所以 只要start[i] == R时候 end[j] ==R 切 r>=j 就可以了
##### 最后在考虑 当i或j一个到头了另一个没到头
##### 那么另一个就必须后面全是X ,用for循环遍历一下
start = "X"
end = "R"

start = "RXXLRXRXL"
end = "XRLXXRRLX"
# #
start = "RXXLRXRXL"
end = "XRLXXRRLL"
#
start = "XLLR"
end = "LXLX"
# #
start = "XXXLXXXXXX"
end = "XXXLXXXXXX"

start = "XXRXXLXXXX"
end = "XXXXRXXLXX"
class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i = j = 0
        count_i = count_j = 0
        length = len(end)

        while i < length and j <length:

            if start[i] == "X" :
                if i <= ((length -1)):
                    i += 1
                    count_i += 1
                    continue
                else:
                    break
            if end[j] == "X" :
                if j <= (length - 1):
                    j += 1
                    count_j += 1
                    continue
                else:
                    break

            if start[i] == end[j]:
                # if not(start[i] == "R" and i <=j):
                #     return False
                # if not(start[j] == "L" and i >=j):
                #     return False
                if (start[i] == "R" and i <=j) or (start[i] == "L" and i >=j):
                    i = i + 1
                    j = j + 1
                else:
                    return False
                # if not(start[j] == "L" and i >=j):
                #     i = i + 1
                #     j = j + 1
                # else:
                #     return False
                # i = i + 1
                # j = j + 1
            else :
                return False

        if i < length:
            for idx in range(i,length):
                if start[idx] != "X":
                    return False
        if j < length:
            for idx in range(j,length):
                if end[idx] != "X":
                    return False

        return  True

a = Solution()
q = a.canTransform(start,end)
print("q=",q)