class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        for x in range(1, n + 1):
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        
        return -1
