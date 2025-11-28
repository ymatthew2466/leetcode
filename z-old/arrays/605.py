# 605. Can Place Flowers


from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Every-other plot AT MOST

        at each index: if left||right is populated --> invalid
            greedy (do whenever we can)
        
        Condition for valid

        bool LEFT IS FREE:
            flowerbed[index-1] == 0 || index == 0
        
        BOOL RIGHT IS FREE:
            flowerbed[index+1] == 0 || index == len(flowerbed)-1
        
        if LEFT && RIGHT:
            flowerbed[index] = 1
            PLANT!!
        '''
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            # left = False
            # right = False
            left = i==0 or (i>0 and flowerbed[i-1]==0)
                # left = True
            right = i==len(flowerbed)-1 or (i<len(flowerbed)-1 and flowerbed[i+1])==0
                # right = True
            if left and right:
                flowerbed[i] = 1
                count += 1
        return count >= n