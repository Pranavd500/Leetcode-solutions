class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        # Find the largest element in the array
        maximum = max(nums)
        
        # Find the smallest element in the array
        minimum = min(nums)
        
        # Best possible subarray value
        best_value = maximum - minimum
        
        # Since we can reuse the same subarray k times
        return best_value * k