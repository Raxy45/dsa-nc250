class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-k
        while l<=r:
            mid = (l+r)//2
            # print(mid, l, r)
            # print(arr[l], arr[r+1])
            if abs(arr[l] - x) <= abs(arr[r+1] - x):
                r = mid - 1
            else:
                l = mid
        return arr[l:l+k]