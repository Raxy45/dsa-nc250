class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low, high = 0, len(arr)-k-1
        while low<high:
            mid = (low+high)//2
            if abs(arr[mid] - x) > abs(arr[mid+k] - x):
                # This means element just outside the window is better than current mid
                # Therefore we shift the window entirely to RHS, we lose mid and gain mid+k element
                low = mid+1
            else:
                # In this, the element outside the window is away from midth element, therefore
                # we bring the pointer to LHS. But still mid can be in the answer, so we bring 
                # r to mid and not mid - 1
                high = mid
        return arr[low:low+k]