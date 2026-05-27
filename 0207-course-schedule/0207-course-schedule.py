from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):

        # Create graph
        preMap = defaultdict(list)

        for course, pre in prerequisites:
            preMap[course].append(pre)

        visiting = set()

        def dfs(course):

            # Cycle found
            if course in visiting:
                return False

            # No prerequisites left
            if preMap[course] == []:
                return True

            # Mark current course as visiting
            visiting.add(course)

            # Check all prerequisites
            for pre in preMap[course]:

                if not dfs(pre):
                    return False

            # Remove from visiting after done
            visiting.remove(course)

            # Mark as completed
            preMap[course] = []

            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True