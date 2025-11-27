class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        prefix sum

        L -> R:
            each index in array is product up to that point
        L <- R:
            ""
        product of each index is left*right
        '''
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(0, len(nums)):
            if i==0:
                left[i] = nums[i]
                continue
            left[i] = nums[i] * left[i-1]

        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                right[i] = nums[i]
                continue
            right[i] = nums[i] * right[i+1]
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(right[i+1])
            elif i == len(nums)-1:
                res.append(left[i-1])
            else:
                res.append(left[i-1]*right[i+1])
        return(res)