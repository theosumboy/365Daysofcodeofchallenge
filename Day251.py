class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        memo = defaultdict(list)
        n = len(s)
        res = []
        
        def dp(start):
            if start == n: 
                return
            for end in range(start + 1, n + 1):
                # if start to end is in word_set, memo[start] should append the index end to record the path
                if s[start: end] in word_set:
                    memo[start].append(end)
                    # if some path in memo[end], we are not going to call dp(end), just use the recorded path in memo[end] 
                    if not memo[end]:
                        dp(end)
                        
        # Ex: "catsanddog"["cat","cats","and","sand","dog"]  {0: [3, 4], 3: [7], 7: [10], 10: [], 4: [7]})
        # use backtracking to get the result
        
        def getResult(path, start):
            if start == n:
                res.append(" ".join(path))
                return
                
            for index in memo[start]:
                getResult(path + [s[start: index]], index)
        
        
        dp(0)
        getResult([], 0)
        return res    
             
