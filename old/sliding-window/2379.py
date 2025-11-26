# 2379. Minimum Recolors to Get K Consecutive Black Blocks


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        goal: find window of size K, such that, # W is minimized

        0123456789
        WBBWWBBWBW

        window starts with len==k
        [WWBWWBB]BBW
        W[WBWWBBB]BW

        BBWWBBWBBBW, k=3
               ...

        slide the window constantly, keep track of each starting index -> # white
        K: index, V: count
        '''

        l, r = 0, k
        freq = {}  # K: left index, V: #W

        def count_w(s: str):
            count = 0
            for char in s:
                if char == 'W':
                    count += 1
            return count
        freq[0] = count_w(blocks[0:k])


        for i in range(1, len(blocks)-k+1):
            right_ptr = i+k-1  # assumes non-inclusive
            
            left = blocks[i-1]  # this char is leaving
            right = blocks[right_ptr]  # this char is joining

            # set to last window initially
            freq[i] = freq[i-1]

            # only consider the char that's leaving/joining
            if left == 'W':
                freq[i] -= 1
            if right == 'W':
                freq[i] += 1

    
            # # adjust counts based on L/R:
            # if left == 'W' and blocks[i-1] != 'W':
            #     freq[i] += 1
            #     print(f"{i}: inc left")
            # if left != 'W' and blocks[i-1] == 'W':
            #     freq[i] -= 1
            #     print(f"{i}: dec left")

            # if right == 'W' and blocks[right_ptr-1] != 'W':
            #     freq[i] += 1
            #     print(f"{i}: inc right")
            # if right != 'W' and blocks[right_ptr-1] == 'W':
            #     freq[i] -= 1
            #     print(f"{i}: dec right")
        
        print(freq)
        return min(freq.values())