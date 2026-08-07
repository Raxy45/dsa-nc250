class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr = 0
        for i in range(1, len(arr)-1):
            useGt = useLt = True
            for j in range(i+1, len(arr)):
                if (useGt and arr[i] > arr[j]):
                    useGt = False
                    useLt = True
                    curr = max(curr, j-i+1)
                elif useLt and arr[i] < arr[j]:
                    useLt = False
                    useGt = True
                    curr = max(curr, j-i+1)
                else:
                    break
        return curr
            