class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        search = mat[0]
        for num in search:
            found = 1
            for lst in mat[1:]:
                if num not in lst:
                    found = 0
            if found == 1:
                return num
        return -1

        