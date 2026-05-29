DIGIT_LETTER_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        c = []
        if not digits:
            return []
        self.combination(c, "", digits)
        return c
    
    def combination(self, c, comb, digits):
        if len(digits) == 0:
            c.append(comb)
            return
        for l in DIGIT_LETTER_MAP[digits[0]]:
            self.combination(c, comb+l, digits[1:])