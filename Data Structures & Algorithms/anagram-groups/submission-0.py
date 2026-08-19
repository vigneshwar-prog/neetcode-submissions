class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            freq[tuple(count)].append(string)
        return list(freq.values())



        