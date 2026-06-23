class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        ml = mountainArr.length()
        l, r = 0, ml - 1
        while l<=r:
            m = (l+r)//2
            ms1 = mountainArr.get(m-1)
            me = mountainArr.get(m)
            ma1 = mountainArr.get(m+1)
            if ms1 < m < ma1:
                # we are on LHS part
                l = m + 1
            elif ms1 > m > ma1:
                # we are on RHS Part
                r = m - 1
            else:
                # m < ma1 and m>ms1 
                # m is the peak
                break
        
        l, r = 0, m
        while l<=r:
            m1 = (l+r)//2
            m1e = mountainArr.get(m1)

            if m1e == target:
                return m1
            
            if m1e > target:
                r = m1 - 1
            else:
                l = m1 + 1
        
        l, r = m+1, ml -1 
        while l<=r:
            mid = (l+r)//2
            mid_elem=mountainArr.get(mid)
            if mid_elem == target:
                return mid
            
            if mid_elem > target:
                l = mid + 1
            else:
                r = mid - 1
        return -1



