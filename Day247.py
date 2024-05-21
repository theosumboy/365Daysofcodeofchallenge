class Solution(object):
    def subsets(self, nums):
      result = [[]]  # start with the empty set

      for num in nums:
          size = len(result)
          for i in range(size):
              new_subset = list(result[i])
              new_subset.append(num)
              result.append(new_subset)

      return result
