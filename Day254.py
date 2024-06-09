class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l, r, sum = 0, 0, 0
        max_len = 0
        while r<len(s):
            sum += abs(ord(s[r])-ord(t[r]))
            while sum>maxCost:
                sum -= abs(ord(s[l])-ord(t[l]))
                l+=1
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len
