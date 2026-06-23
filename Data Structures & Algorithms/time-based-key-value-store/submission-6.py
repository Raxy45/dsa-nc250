class TimeMap:

    def __init__(self):
        self.hmp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmp:
            self.hmp[key] = []
        self.hmp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmp:
            return ""
        
        mood_mp = self.hmp[key]
        l, r = 0, len(mood_mp)-1
        while l<=r:
            m = (l+r)//2
            if mood_mp[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1
        return mood_mp[m][1]
