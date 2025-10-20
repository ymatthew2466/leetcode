# 2678. Number of Senior Citizens


from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for person in details:
            # age = person[11:11+2]
            if int(person[11:11+2]) > 60:
                count += 1
        return count