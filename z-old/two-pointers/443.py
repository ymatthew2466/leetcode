# 443. String Compression


from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        ptr1 at the start of a unique char

        ptr2 increments to count how many until next unique char

        store count

        at next unique char, update ptr1, ptr2 

        append to string, then set chars to split(string)
        '''
        ptr1 = 0
        ptr2 = 0

        s = ""
        curr = ""
        count = 0
        m = 0

        while ptr1 < len(chars):
            curr = chars[ptr1]
            s += curr
            while ptr2<len(chars) and chars[ptr2] == curr:
                ptr2 += 1
                count += 1
                # print(f"1: {ptr1}, 2: {ptr2}, curr: {curr}, count: {count}")
            if count > 1:
                s += str(count)
            # print(f"s: {s}")
            
            ptr1 = ptr2
            count = 0
        res = [char for char in s]
        chars[:] = res
        return len(chars)
