class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        left, right pointers
        find sum
        if sum > target, we need to reduce -> decrement right ptr
        if sum < target, increase sum by incrementing left
        '''
        res = []
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                res.append(l+1)
                res.append(r+1)
                return res
            if s < target:
                # increase sum by incrementing left
                l += 1
            if s > target:
                # dec sum by dec right
                r -= 1
        return res