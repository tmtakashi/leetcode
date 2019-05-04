class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]  # dp[n] means the maximum sum of
        # the subarrays ends with the nth element

        for i in range(1, len(nums)):
            if nums[i] + dp[i - 1] < nums[i]:
                dp.append(nums[i])
            else:
                dp.append(nums[i] + dp[i - 1])

        return max(dp)
