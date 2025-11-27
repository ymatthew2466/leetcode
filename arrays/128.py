class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        convert nums to set
        visited set
        
        for each num:
            check if it's the top of the chain
            if top:
                check if number immediately lower is in set
                if yes:
                    increment streak
                    add to visited
        '''
        if len(nums) == 0:
            return 0
        nums = set(nums)
        longest = float("-inf")
        for num in nums:
            if num+1 in nums:
                continue
            # top of chain
            curr = num
            streak = 0
            while curr in nums:
                curr -= 1
                streak += 1
                print(f"num: {num}, curr: {curr}, streak: {streak}")
            longest = max(streak, longest)
        return longest
                

        

            