class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_finished = set()
        prerequisites.sort(key=lambda x: x)
        for pair in prerequisites:
            print(pair)
            actual_course, pre_req  = pair
            if actual_course in courses_finished:
                return False
            
            courses_finished.add(pre_req)
        
        return True