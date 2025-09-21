# 15. 3Sum


from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort array first (ascending)

        interate i thru arr:
            l = i+1
            r = len(nums)-1
            while l<r:
                three = arr[i] + arr[l] + arr[r]
                if three < 0:
                    find way to increase the sum (move left pointer up)
                if three > 0:
                    find way to lower the sum (move right pointer down)
        '''
        nums.sort()
        res = []
        # existing = set()

        for i in range(len(nums)):
            # skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                three = nums[i] + nums[l] + nums[r]
                # print(f"i: {i}, l: {l}, r: {r}, three: {three}")
                if three == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    # if (nums[i], nums[l], nums[r]) not in existing:
                    #     existing.add((nums[i], nums[l], nums[r]))
                    #     res.append([nums[i], nums[l], nums[r]])
                    # continue finding triplets for i
                    l += 1
                    r -= 1
                    # skip duplicates
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                if three < 0:  # increase sum by incrementing left
                    l += 1
                if three > 0:  # decrease sum by decrementing right
                    r -= 1
        return res