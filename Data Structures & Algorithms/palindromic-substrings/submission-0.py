class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def dfs(left, right):
            if left < 0 or right > len(s) - 1 or s[left] != s[right]:
                return
            word = s[left : right + 1]
            res.append(word)
            dfs(left - 1, right + 1)

        for i in range(len(s)):
            dfs(i, i + 1) # for even palindromes
            dfs(i, i) # for odd palindromes
        return len(res)