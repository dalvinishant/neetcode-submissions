class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = [""]

        def dfs(left, right):
            if left < 0 or right > len(s) - 1 or s[left] != s[right]:
                return
            word = s[left : right + 1]
            if len(word) > len(res[0]):
                res[0] = word
            dfs(left - 1, right + 1)

        for i in range(len(s)):
            dfs(i, i + 1) # for even palindromes
            dfs(i, i) # for odd palindromes
        return res[0]