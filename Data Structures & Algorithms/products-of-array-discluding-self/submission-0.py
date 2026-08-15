class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,4,6]
        [48,48,24,6]
        48
        24
        12
        '''
        n = len(nums)
        product_list = [1] * n
        product = 1
        for i in range(n-1,-1,-1):
            product_list[i] = product*nums[i]
            product = product * nums[i]
        final = []
        product = 1
        for i in range(n):
            if i == 0:
                final.append(product_list[1])
            elif i == n-1:
                final.append(product)
            else:
                final.append(product*product_list[i+1])
            product = product * nums[i]
        return final

             

        