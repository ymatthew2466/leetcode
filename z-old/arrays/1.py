# 1. Two Sum

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # K: target-elt, V: index
        # check if the current element is in the dict, if so, return [i, dict[i]]

        d = {}  # K: diff, V: index
        for i in range(len(nums)):
            elt = nums[i]
            if elt in d:
                return [i, d[elt]]
            else:
                d[target-elt] = i