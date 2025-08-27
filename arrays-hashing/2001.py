# 2001. Number of Pairs of Interchangeable Rectangles

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        '''
        K: ratio, V: [rectangles]
            - sort into buckets
            - take value list, then run backtracking to get all combinations
        
        def backtrack(rect_pair, full_list, index):
            if len(rect_pair) == 2:
                pair is formed
                count ++ or append to list
            
        '''
        res = []
        count = 0
        def backtrack(rect_pair, full_list, start_index):
            nonlocal count
            if len(rect_pair) == 2:
                # pair formed
                # res.append(rect_pair[:])
                count += 1
                return
            
            # recursive call
            for i in range(start_index, len(full_list)):
                rect_pair.append(full_list[i])
                backtrack(rect_pair, full_list, i+1)
                rect_pair.pop()


        buckets = {}
        for rect in rectangles:
            ratio = rect[0]/rect[1]
            buckets[ratio] = buckets.get(ratio, [])
            buckets[ratio].append(rect)
        
        # for ratio in buckets:
        #     backtrack([], buckets[ratio], 0)
        
        for ratio in buckets:
            n = len(buckets[ratio])
            count += n * (n - 1) // 2
        
        return count