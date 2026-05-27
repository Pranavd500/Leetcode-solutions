class Solution:
    def merge(self, intervals):
        
        # Step 1: Sort intervals by starting time
        intervals.sort()

        merged = []

        for interval in intervals:

            # If merged list is empty
            # OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                # Overlap found
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged