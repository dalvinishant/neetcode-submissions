import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_freq  = {}
        for t in tasks:
            if t in task_freq:
                task_freq[t] += 1
            else:
                task_freq[t] = 1
        task_freq = [cnt for _, cnt in task_freq.items()]
        heapq.heapify_max(task_freq)

        # queue for tracking execution with cooldown
        q = []
        time = 0
        while task_freq or q:
            time += 1

            if not task_freq:
                time = q[0][1]
            else:
                cnt = heapq.heappop_max(task_freq) - 1
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush_max(task_freq, q.pop(0)[0])
        
        return time