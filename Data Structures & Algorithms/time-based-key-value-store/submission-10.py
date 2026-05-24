class TimeMap:
    # When you want largest value just below target > use r
    # When you want value just after the target     > use l 

    def __init__(self):
        self.hmp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmp:
            self.hmp[key] = []
        self.hmp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmp: return ""

        ls = self.hmp[key]
        if timestamp<ls[0][0]: return ""
        l, r= 0, len(ls)-1
        if timestamp>ls[r][0]: return ls[r][1]
        while l<=r:
            m = (l+r)//2
            if ls[m][0] == timestamp:
                return ls[m][1]
            
            if ls[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        return ls[r][1]
