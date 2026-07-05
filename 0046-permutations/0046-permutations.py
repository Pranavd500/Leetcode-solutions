class Solution:
    def permute(self, nums):

        result = []

        def backtrack(path):

            # Found one permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:

                # Skip numbers already used
                if num in path:
                    continue

                # Choose
                path.append(num)

                # Explore
                backtrack(path)

                # Undo choice
                path.pop()

        backtrack([])

        return result