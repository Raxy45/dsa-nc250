class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        low, high = 0, len(arr)-k-1
        while low<=high:
            mid = (low+high)//2
            if abs(arr[mid]-x) > abs(arr[mid+k]-x):
                low = mid+1
            else:
                high = mid -1
        print(low, mid, high)
        return arr[low:low+k]