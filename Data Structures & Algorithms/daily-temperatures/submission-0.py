class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        # iterate through the temperatures
        for i, t in enumerate(temperatures):
            # check stack if the top is lesser than current and update the res
            while st and t > st[-1][0]:
                stemp, sind = st.pop()
                res[sind] = i - sind
            st.append((t, i))
        return res