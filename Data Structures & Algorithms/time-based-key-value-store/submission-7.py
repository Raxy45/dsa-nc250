class TimeMap:

    def __init__(self):
        self.hmp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmp:
            self.hmp[key] = []
        self.hmp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmp: return ""

        ls = self.hmp[key]
        l, r= 0, len(ls)-1
        while l<=r:
            m = (l+r)//2
            if ls[m][0] == timestamp:
                return ls[m][1]
            
            if ls[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        print(ls, timestamp, l, m, r)
        return ls[m][1]
