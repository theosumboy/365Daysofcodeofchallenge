class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        bitSize = 1 << n
        res = 0

        for i in range(bitSize):
            curr = 0
            for j in range(n):
                if i & (1 << j):
                    curr ^= nums[j]
            res += curr

        return res
