class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key][0].append(timestamp)
            self.data[key][1].append(value)
        else:
            self.data[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        print(self.data)
        if key not in self.data:
            return ""

        timestamps = self.data[key][0]
        l, r = 0, len(timestamps)-1
        mid = -1
        print(timestamps)
        while l<=r:
            mid = (l+r)//2
            if timestamps[mid] == timestamp:
                return self.data[key][1][mid]
            
            if timestamps[mid]<timestamp:
                l = mid+1
            else:
                r = mid-1
        return self.data[key][1][r]
