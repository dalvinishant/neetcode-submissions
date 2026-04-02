class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: 
            return True
        edges = defaultdict(set)
        courses = set()
        for c, p in prerequisites:
            if c == p or (p in edges and c in edges[p]):
                return False
            edges[c].add(p)
            courses.add(c)
            courses.add(p)
        return len(courses) != len(edges)