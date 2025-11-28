class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        SORT!!
        each num in nums is a target (negative)
        for each num in nums:
            2 pointer approach 
            see if nums[l] + nums[r] == -num
        
        check duplicates:
            if consecutive equal numbers, skip until unique number
            --> FOR main loop AND while loop
        '''
        nums = sorted(nums)
        res = []
        def matchTarget(target, left, right):
            res = []
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([-target, nums[left], nums[right]])
                    # check next values
                    left += 1
                    right -= 1
                    # skip dupes
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            return res
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            matched = matchTarget(-num, i+1, len(nums)-1)
            if len(matched)>0:
                res.extend(matched)
        return(res)