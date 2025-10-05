# 207. Course Schedule

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visit set holds all courses along curr DFS path
        visited = set()

        def dfs(crs):
            # base cases
            if crs in visited:  # visit course twice (CYCLE)
                return False
            if preMap[crs] == []:  # no prereqs, VALID
                return True
            visited.add(crs)

            # return false if not valid
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            # if we make it here, the course can be taken
            
            # finished visiting this crs
            visited.remove(crs)

            # since we know this course can be completed
            preMap[crs] = []

            # if we exit loop, possible
            return True
        
        # run DFS on all courses b/c what if graph isn't fully connected
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True