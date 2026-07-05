class Solution:

    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]

        # House Robber I
        def helper(arr):
            prev2 = 0
            prev1 = 0

            for money in arr:
                current = max(prev1, prev2 + money)

                prev2 = prev1
                prev1 = current

            return prev1

        return max(
            helper(nums[:-1]),   # Exclude last house
            helper(nums[1:])     # Exclude first house
        )