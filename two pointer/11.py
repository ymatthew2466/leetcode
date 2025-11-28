class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        store global max area

        only way moving closer to center is better is if height is more

        increment left / decrement right until we find height that's greater than curr
        find new area
        update global max
        '''
        most = float("-inf")
        l = 0
        r = len(height)-1
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            area = w * h
            most = max(most, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return(most)