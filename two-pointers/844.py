# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        backspace:
        - remove last char
        - if empty, still empty
        '''
        
        def prune(input: str):
            res = ""
            for char in input:
                if char != "#":
                    res += char
                else:
                    res = res[:len(res)-1] if len(res) > 0 else ""
            return res
            
        return prune(s) == prune(t)


# =============================== #
# test cases copied from LeetCode #
# =============================== #

if __name__ == "__main__":
    s = Solution()

    # test case 1
    s1 = "ab#c"
    t1 = "ad#c"
    assert s.backspaceCompare(s1, t1) is True

    # test case 2
    s2 = "ab##"
    t2 = "c#d#"
    assert s.backspaceCompare(s2, t2) is True

    # test case 3
    s3 = "a#c"
    t3 = "b"
    assert s.backspaceCompare(s3, t3) is False

    # test case 4
    s4 = "a##c"
    t4 = "#a#c"
    assert s.backspaceCompare(s4, t4) is True

    print("All test cases passed")
