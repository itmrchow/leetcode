
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        # enumerate列舉
        for i, v in enumerate(nums):
            d = target-v
            if d not in h:
                h[v] = i
            else:
                return [h[d], i]


s = Solution()
a = s.twoSum([2, 7, 11, 15], 9)
print(a)
