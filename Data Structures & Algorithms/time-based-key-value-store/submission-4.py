class TimeMap:

    def __init__(self):
        self.log = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.log:
            self.log[key] = {}
            if timestamp not in self.log[key]:
                self.log[key] = {timestamp: value}
        else:
            self.log[key][timestamp] = value
        pass

    def get(self, key: str, timestamp: int) -> str:
        if key in self.log:
            if timestamp in self.log[key]:
                return self.log[key][timestamp]
            else:
                return self.searchLast(key, timestamp)
        return ""
    
    def searchLast(self, key, target: int) -> str:
        logs = list(self.log[key].keys())
        print(logs)
        left, right = 0, len(logs) - 1
        while left < right:
            mid = (left + right) // 2
            
            if mid == left:
                break

            if target > logs[mid]:
                left = mid
            else:
                right = mid
        lastNum = logs[right] if logs[right] < target else logs[left]
        print(logs, lastNum, target)
        return self.log[key][lastNum] if lastNum in self.log[key] and lastNum <= target else ""

