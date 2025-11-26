class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        add to set, if already in, return false
        '''
        unique = set()
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False