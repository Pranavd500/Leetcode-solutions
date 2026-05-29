class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s


        start =0
        max_len= 1
        def expand(left, right):
            #check
            while left >= 0 and right < len(s) and s[left] == s[right]:
                
                left -=1
                right +=1
            return right - left - 1
        
        for i in range(len(s)):
            odd_len=expand(i,i)
            even_len=expand(i,i+1)
            current_max=max(odd_len,even_len)

            if current_max > max_len:
                max_len = current_max
                start = i - (current_max-1) // 2
                
        return s[start:start + max_len]