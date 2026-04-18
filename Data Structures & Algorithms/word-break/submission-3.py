class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.buildWord('', s, wordDict, {})
    
    def buildWord(self, c, s, words, mem):

        if c in mem:
            return mem[c]

        if len(c) > len(s):
            mem[c] = False
            return mem[c]

        if c == s:
            mem[c] = True
            return mem[c]
        
        for j in words:
            new_c = c + j
            if s.startswith(new_c):
                exists = self.buildWord(new_c, s, words, mem)
                if exists:
                    mem[c] = True
                    return mem[c]

        mem[c] = False
        return mem[c]