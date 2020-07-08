class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = len(strs)
        pairs = [(s.count('0'), len(s) - s.count('0')) for s in strs]
        # print("pairs",pairs)
        # formed_ix:已拼出数组索引，用了多少个m，多少个n，已form num
        state_dict = {"formed_ix": [],
                      "m": 0,
                      "n": 0,
                      "num": 0}

        for i in range(l):
            self.update(state_dict, pairs, i, m, n)

        return state_dict["num"]

    def update(self, state_dict, pairs, index, m, n):
        if m - state_dict['m'] >= pairs[index][0] and n - state_dict['n'] >= pairs[index][1]:
            state_dict['formed_ix'].append(index)
            state_dict['m'] += pairs[index][0]
            state_dict['n'] += pairs[index][1]
            state_dict['num'] += 1
        else:
            formed_ix = state_dict['formed_ix']
            for i in range(index):
                if i not in formed_ix:
                    for j in formed_ix:
                        zeros = pairs[i][0] + pairs[index][0]
                        ones = pairs[i][1] + pairs[index][1]

                        remain_zeros = m - state_dict['m'] + pairs[j][0]
                        remain_ones = n - state_dict['n'] + pairs[j][1]

                        if zeros <= remain_zeros and ones <= remain_ones:
                            formed_ix.remove(j)
                            formed_ix.append(i)
                            formed_ix.append(index)
                            state_dict['m'] += zeros - pairs[j][0]
                            state_dict['n'] += ones - pairs[j][1]
                            state_dict['num'] += 1
                            return


strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

strs = ["10", "0", "1"]
m = 1
n = 1

strs = ["111", "1000", "1000", "1000"]
m = 9
n = 3

strs = ["011", "1", "11", "0", "010", "1", "10", "1", "1", "0", "0", "0", "01111", "011", "11", "00", "11", "10", "1",
        "0", "0", "0", "0", "101", "001110", "1", "0", "1", "0", "0", "10", "00100", "0", "10", "1", "1", "1", "011",
        "11", "11", "10", "10", "0000", "01", "1", "10", "0"]
m = 44
n = 39
print(Solution().findMaxForm(strs, m, n))
