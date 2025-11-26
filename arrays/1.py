class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        must be O(N)
        
        dict
        K: num, V: index

        loop thru and store each num/index pair
        
        for each num, check if target-num is in dict
        return both indices
        '''
        dic = {}
        for i in range(len(nums)):
            num = nums[i]

            if target-num in dic:
                return [i, dic[target-num]]
            dic[num] = i
        return []