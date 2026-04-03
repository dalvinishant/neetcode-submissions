class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ops = self.equate(word1, word2, {})
        return ops
    
    def equate(self, s1, s2, mem):
        if s1 == s2: 
            return 0

        if not s1:
            return len(s2)
        
        if not s2:
            return len(s1)
        
        if (s1, s2) in mem:
            return mem[(s1, s2)]
        
        if s1[0] == s2[0]:
            return self.equate(s1[1:], s2[1:], mem)
        
        # insert
        op_i = 1 + self.equate(s1, s2[1:], mem)

        # delete
        op_d = 1 + self.equate(s1[1:], s2, mem)

        # replace
        op_r = 1 + self.equate(s1[1:], s2[1:], mem)

        mem[(s1, s2)] = min(op_i, op_d, op_r)

        return mem[(s1, s2)]