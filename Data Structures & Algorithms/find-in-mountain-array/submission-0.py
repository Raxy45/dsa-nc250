class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        if mountainArr.length()<3:
            return -1

        peak = -1
        low, high = 0, mountainArr.length()-1
        while low<=high:
            mid = (low+high)//2
            if mountainArr.get(mid)>mountainArr.get(low):
                low=mid
            else:
                high = mid-1
        peak = low
        print('peak ', peak)
        low, high = 0, peak
        print(low, high, 'first')
        while low<=high:
            mid = (low+high)//2
            print('mid', mid)
            print(mountainArr.get(mid), target)
            if mountainArr.get(mid)==target:
                print('found')
                return mid
            elif mountainArr.get(mid)>target:
                high=mid-1
            else:
                low=mid+1
        
        low, high = peak+1, mountainArr.length()-1
        while low<=high:
            mid = (low+high)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                high=mid-1
            else:
                low=mid+1
        return -1