import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:

            if i not in "+*-/":
                st.append(i)
            else:
                r_op = int(st.pop(-1))
                l_op = int(st.pop(-1))
                if i == '+':
                    ans = l_op + r_op
                elif i == '-':
                    ans = l_op - r_op
                elif i == '*':
                    ans = l_op * r_op
                elif i == '/':
                    ans = math.trunc(l_op/r_op)
                st.append(ans)

        return int(st.pop(-1))
