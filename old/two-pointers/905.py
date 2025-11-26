# 905. Sort Array By Parity


from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        '''
        2 ptr approach
        left ptr = 0
        right ptr = end of lst

        when insert even, shift left ptr += 1
        when insert odd, shift right ptr -= 1
        '''
        if len(nums)==0:
            return []
        
        res = [0] * len(nums)
        # print(res)
        l = 0
        r = len(res)-1
        for num in nums:
            if num%2==0:
                res[l] = num
                l += 1
            else:
                res[r] = num
                r -= 1
        return res
        
        '''
        1 ptr approach
        '''
        # even = []
        # odd = []
        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)
        # even.extend(odd)
        # return even