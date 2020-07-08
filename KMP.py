#-*- coding:utf-8 -*-
#@Date   : 2018/12/24
#@Author : suyifan
#@File   : KMP.py


# s = "aabaabaaa"
# t = "aabcaabaacaabaabaaa"

#
# def temp_array(str1):
#     n = len(str1)
#     array = [0] * n
#     # for i,c in enumerate(str1):
#     array[0] = 0
#     left = 0
#     right = 1
#     while right < n:
#         if str1[right] == str1[left]:
#             array[right] = left + 1
#             left += 1
#             right += 1
#         else:
#             # if array[left-1] != 0 : #todo
#             if left != 0:
#                 left = array[left-1]
#             else:
#                 # left = 0
#                 array[right] = 0
#                 right += 1
#     return array
#
# def kmp(s,t):
#     s_len = len(s)
#     t_len = len(t)
#     array = temp_array(s)
#
#     idx_s = 0
#     idx_t = 0
#     while idx_t < t_len and idx_s < s_len:
#         if s[idx_s] == t[idx_t]:
#             idx_s += 1
#             idx_t += 1
#         else:
#             if idx_s != 0:
#                 idx_s = array[idx_s-1]
#             else:
#                 idx_t += 1
#     if idx_s == s_len:
#         return idx_t - s_len
#     return 0
#
# print(s)
# print(t)
# print(temp_array(s))
# print(kmp(s,t))
# print(temp_array(str1))

short = "aabaabaaa"
long = "aabcaabaacaabaabaaazz"

def temp_array(short):
    if not short:
        return
    n = len(short)
    array = [0] * n
    left = 0
    right = 1
    while right < n:
        if short[left] == short[right]:
            array[right] = left + 1
            left += 1
            right += 1
        else:
            if left != 0:
                left = array[left-1]
            else:
                right += 1
    return array
def kmp(short,long):
    idx_short = idx_long = 0
    len_short = len(short)
    len_long = len(long)
    array = temp_array(short)

    while idx_long < len_long and idx_short < len_short:
        if short[idx_short] == long[idx_long]:
            idx_short += 1
            idx_long += 1
        else:
            if idx_short != 0:
                idx_short = array[idx_short-1]
            else:
                idx_long += 1
    if idx_short == len_short:
        return idx_long - len_short
    return -1


print(short)
print(long)
print(temp_array(short))
print(kmp(short,long))