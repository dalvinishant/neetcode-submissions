class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in res:
                res[key] = []
                for j in range(i, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        res[key].append(strs[j])
                        
        return [list(val) for _, val in res.items() if val]