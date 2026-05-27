class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store: {value: index}
        prevMap = {} 
        
        for i, n in enumerate(nums):
            diff = target - n
            # If the complement exists in the map, we found the pair
            if diff in prevMap:
                return [prevMap[diff], i]
            # Otherwise, add current number and its index to the map
            prevMap[n] = i
        
        return [] 