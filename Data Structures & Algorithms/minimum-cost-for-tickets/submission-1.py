class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        min_cost = self.calculateMinCost(0, days, costs, {})
        return min_cost
    
    def calculateMinCost(self, i, days, costs, mem):
        if i == len(days):
            # print('returning')
            return 0
        if i in mem:
            return mem[i]
        
        opt_1 = costs[0] + self.calculateMinCost(i+1, days, costs, mem)
        
        i_7 = i
        for j in range(i, len(days)):
            if days[j] > days[i] + 6:
                break
            i_7 = j
        # print('--',i, i_7, days[i], days[i_7])

        opt_7 = costs[1] + self.calculateMinCost(i_7+1, days, costs, mem)

        i_30 = i
        for j in range(i, len(days)):
            if days[j] > days[i] + 29:
                break
            i_30 = j

        opt_30 = costs[2] + self.calculateMinCost(i_30+1, days, costs, mem)
        min_cost = min(opt_1, opt_7, opt_30)
        mem[i] = min_cost
        
        return min_cost
        

            