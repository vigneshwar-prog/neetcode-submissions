class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        freq = {}
        longest = 0
        for end in range(len(s)): 
            freq[s[end]] = freq.get(s[end],0) + 1
            while freq[s[end]] > 1:
                freq[s[start]] -= 1
                start += 1

            longest = max(end-start + 1,longest)
        return longest

        