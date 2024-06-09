class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = int(s, 2)
        
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            steps += 1
        
        return steps
