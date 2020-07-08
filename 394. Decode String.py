#-*- coding:utf-8 -*-
#@Date   : 2019/1/10
#@Author : suyifan
#@File   : 394. Decode String.py

s = "3[a2[c]]" # ans = accaccacc
s = "3[a]2[bc]"# 返回 "aaabcbc".
s = "2[abc]3[cd]ef"# 返回 "abcabccdcdcdef"
s = "2[ab]3[c]"
s = "leetcode"
s = "100[leetcode]"
s = "3[a]2[b4[F]c]" #ans = "aaabFFFFcbFFFFc"
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        stack = []
        ans = ""
        str1 = ""
        num = ""
        for i in s:

            if i == "]":
                str1 = ""
                while stack:

                    q = stack.pop()
                    if q == "[":
                        if stack:
                            stack.append(str1)
                        else:
                            ans += str1
                        # stack.append(str1)
                        str1 = ""
                        break
                        # ans += str1
                    elif q.isdigit():
                        str1 *= int(q)
                        # str1 = ""
                    else:
                        str1 = q + str1

                str1 = ""
            else:
                if i.isdigit():
                    num += i
                else:
                    if num:
                        stack.append(num)
                        num = ""
                    stack.append(i)
        print(stack)
        str1 = ""
        num = 1
        while stack:
            q = stack.pop(0)
            if q.isdigit():
                num = q
            else:
                ans += q * int(num)
                num = 1
        return ans
        # while stack:
        #     q = stack.pop()
        #     if q == "[":
        #         stack.append(str1)
        #         str1 = ""
        #         # ans += str1
        #     elif q.isdigit():
        #         str1 *= int(q)
        #         # str1 = ""
        #     else:
        #         str1 = q + str1
        # ans += str1
        return ans

        # class Solution:
        #     def decodeString(self, s):
        #         """
        #         :type s: str
        #         :rtype: str
        #         """
        #         if not s:
        #             return ""
        #         stack = []
        #         ans = ""
        #         str1 = ""
        #         num = ""
        #         for i in s:
        #
        #             if i == "]":
        #                 str1 = ""
        #                 while stack:
        #                     q = stack.pop()
        #                     if q == "[":
        #                         stack.append(str1)
        #                         str1 = ""
        #                         # ans += str1
        #                     elif q.isdigit():
        #                         str1 *= int(q)
        #                         # str1 = ""
        #                     else:
        #                         str1 = q + str1
        #                 ans += str1
        #                 str1 = ""
        #             else:
        #                 if i.isdigit():
        #                     num += i
        #                 else:
        #                     if num:
        #                         stack.append(num)
        #                         num = ""
        #                     stack.append(i)
        #         while stack:
        #             q = stack.pop()
        #             if q == "[":
        #                 stack.append(str1)
        #                 str1 = ""
        #                 # ans += str1
        #             elif q.isdigit():
        #                 str1 *= int(q)
        #                 # str1 = ""
        #             else:
        #                 str1 = q + str1
        #         ans += str1
        #         return ans

        #         while stack[-1] != "[":
        #             q = stack.pop()
        #             if q.isdigit():
        #                 str1 *= int(q)
        #             else:
        #                 str1 = q+str1
        #         # ans += str1
        #         stack.pop()
        #         stack.append(str1)
        #     else:
        #         stack.append(i)
        # print(stack)
        # ans = ""
        # str1 = ""
        # while stack :
        #     if stack[-1].isdigit():
        #         ans = str1 * int(stack.pop()) + ans
        #         str1 = ""
        #     else:
        #         str1 = stack.pop()+str1


        # return ans




        # if idx == len(s):
        #     return ""
        # stack_num = [1]
        # stack_str = []
        # ans = ""
        # str1 = ""
        # n = len(s)
        # for i in range(idx,n):
        #     if s[i].isdigit():
        #         stack_num.append(int(s[i]))
        #         stack_str.append(str1)
        #         str1 = ""
        #         # stack_num = int(s[i])
        #     elif s[i] == "[":
        #         str1 += self.decodeString(s,i+1)
        #     elif s[i] == "]":
        #         stack_str.append(str1)
        #
        #         while stack_str:
        #             ans = stack_str.pop()*stack_num.pop() + ans
        #
        #         # ans += str1*stack_num.pop()
        #         return ans
        #     else:
        #         str1 += s[i]
        # return ans
if __name__ == "__main__":
    a = Solution()
    q = a.decodeString(s)
    print("q =",q)