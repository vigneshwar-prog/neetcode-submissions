class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(list)
        freq_t = defaultdict(list)
        for i in s:
            freq[i] = freq.get(i,0) + 1
        for i in t:
            freq_t[i] = freq_t.get(i,0) + 1
        if freq == freq_t:
            return True
        return False
        