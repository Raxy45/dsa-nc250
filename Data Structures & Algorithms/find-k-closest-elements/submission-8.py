class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k
        print(l, r)
        mid = 0
        while l<r:
            mid = (l+r)//2
            print(mid, l, r)
            # print(arr[l], arr[r+1])
            if arr[mid] - x <= arr[mid+k]-x:
                r = mid - 1
            else:
                l = mid + 1
        return arr[mid:mid+k]