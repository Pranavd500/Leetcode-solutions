class Solution:
    def subsets(self, nums):
        result = []
        subset = []

        def dfs(index):

            # Reached the end
            if index == len(nums):
                result.append(subset[:])   # copy
                return

            # Include current number
            subset.append(nums[index])
            dfs(index + 1)

            # Backtrack
            subset.pop()

            # Exclude current number
            dfs(index + 1)

        dfs(0)
        return result