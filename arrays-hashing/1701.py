# 1701. Average Waiting Time

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        '''
        cust[i] = [arrival time, time needed]

        arrival time can overlap with prev order
        [1, 2] means done at 3
        [2, 2] means start at 3, end at 5

        - iterate thru customers
        - track time done with each order (update curr_time int)
        - track time waited in dict:
            - k: index, v: wait time
        '''
        curr_time = customers[0][0]
        wait_total = 0

        for i in range(len(customers)):
            arrival, duration = customers[i][0], customers[i][1]
            curr_time += duration

            # user waiting for prev order
            if curr_time > arrival:
                wait = curr_time - arrival
            else:
                wait = duration
                curr_time = arrival + duration
            wait_total += wait
        
        return wait_total / len(customers)


# =============================== #
# test cases copied from LeetCode #
# =============================== #

if __name__ == "__main__":
    sol = Solution()

    # test case 1
    customers1 = [[1, 2], [2, 5], [4, 3]]
    assert sol.averageWaitingTime(customers1) == 5.0

    # test case 2
    customers2 = [[5, 2], [5, 4], [10, 3], [20, 1]]
    assert sol.averageWaitingTime(customers2) == 3.25

    print("All test cases passed")