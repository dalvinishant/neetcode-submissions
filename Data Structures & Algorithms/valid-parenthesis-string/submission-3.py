class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        ch_st = []

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == '*':
                ch_st.append(i)
            else:
                if not st and not ch_st:
                    return False
                if st:
                    st.pop()
                elif ch_st:
                    ch_st.pop()
                
        while st and ch_st:
            if st.pop() > ch_st.pop():
                return False
        return not st