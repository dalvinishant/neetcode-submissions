class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c in '[{(':
                st.append(c)
            
            if c in '}])':
                if not st:
                    return False
                top = st.pop(-1)
                if (c == ")" and top != '(') or (c == ']' and top != '[') or (c == '}' and top != '{'):
                    return False

        if st:
            return False

        return True