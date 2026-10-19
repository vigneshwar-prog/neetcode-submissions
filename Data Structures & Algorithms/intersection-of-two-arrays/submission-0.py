class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for num in nums1:
            if num not in freq:
                freq[num] = 1
        ans = []
        for num in nums2:
            if num in freq:
                if freq[num] == 1:
                    freq[num] = 2
                    ans.append(num)
        return ans
        