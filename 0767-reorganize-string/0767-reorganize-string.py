class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        # impossible case
        max_freq = max(freq.values())

        if max_freq > (len(s) + 1) // 2:
            return ""

        # max heap
        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))

        result = []

        prev_count = 0
        prev_char = ""

        while heap:

            count, ch = heapq.heappop(heap)

            result.append(ch)

            # decrease frequency
            count += 1

            # push previous back
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            prev_count = count
            prev_char = ch

        return "".join(result)