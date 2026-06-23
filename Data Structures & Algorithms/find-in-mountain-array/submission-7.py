class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, h = 0, mountainArr.length()-1
        while l<=h:
            m = (l+h)//2

            prev = mountainArr.get(m-1)
            mid = mountainArr.get(m)
            next = mountainArr.get(m+1)
            if prev < mid < next:
                # increasing
                l = m+1
            elif prev > mid > next:
                h = m -1
            else:
                break
        
        print(l, m, h)
        print('peak', mountainArr.get(m))
        l, h = 0, m
        while l<=h:
            m = (l+h)//2
            current_elem = mountainArr.get(m)
            if current_elem == target:
                return m
            
            if current_elem < target:
                l = m + 1
            else:
                h = m - 1
        
        l, h = m+1, mountainArr.length()-1
        print('end', l, h)
        while l<=h:
            m = (l+h)//2
            current_elem = mountainArr.get(m)
            if current_elem == target:
                return m
            
            if current_elem > target:
                l = m + 1
            else:
                h = m - 1

        return -1