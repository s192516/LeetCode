#-*- coding:utf-8 -*-
#@Date   : 2018/12/30
#@Author : suyifan
#@File   : 904. Fruit Into Baskets.py


tree = [0,1,2,2]
tree = [3,3,3,1,2,1,1,2,3,3,4] # and = 5
tree = [0,1,6,6,4,4,6] # ans = 5
tree = [6,2,1,1,3,6,6] #ans = 3
tree = [0,1,1]
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        a, b, c = 0, 0, 0
        n = len(tree)
        ans = 0
        idx_a,idx_b = 0,0


        while c < n:
            if tree[c] == tree[idx_a] or tree[c] == tree[idx_b]:
                if tree[c] == tree[a]:
                    idx_a = c
                else:
                    idx_b = c
            elif tree[idx_a] == tree[idx_b]:
                # b = c
                idx_b = c
            else:
                # c += 1
                break
            c += 1
        if c - a > ans:
            ans = c- a
        a = min(idx_a,idx_b) +1
        b = c
        idx_a = a
        idx_b = b
        c += 1



        while c < n:
            if tree[c] == tree[a] or tree[c] == tree[b]:
                if tree[c] == tree[a]:
                    idx_a = c
                else:
                    idx_b = c
            else:
                ans = max(c-a,ans)
                a = max(min(idx_a,idx_b)+1,b)
                b = c
                idx_a = a
                idx_b = b
            c += 1
        ans = max(c-a,ans)
        return ans





        # while c < n:
        #
        #     if tree[c] == num_a or tree[c] == num_b:
        #         if tree[c] == num_b:
        #             idx_b += 1
        #         # else:
        #         if tree[c] == num_a:
        #             idx_a += 1
        #         c += 1
        #     elif not have:
        #         num_b = tree[c]
        #         have = True
        #         idx_b = c
        #         b = c
        #         c += 1
        #     else:
        #         max1 = c-a
        #         if max1 > ans:
        #             ans = max1
        #         # a = max(idx_b,idx_a)
        #         a = min(idx_a,idx_b)+1
        #         b = c
        #         idx_a = a
        #         idx_b = c
        #         num_a = tree[a]
        #         num_b = tree[b]
        #         c += 1
        #     # c += 1
        # if c-a > ans :
        #     ans = c-a
        # return ans


a = Solution()
q = a.totalFruit(tree)
print("q=",q)