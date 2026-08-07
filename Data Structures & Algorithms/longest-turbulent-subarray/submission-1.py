class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        curr = 0
        for i in range(len(arr)-1):
            useGt = useLt = True
            prev = arr[i]
            for j in range(i+1, len(arr)):
                # print(j, useGt, useLt)
                if (useGt and prev > arr[j]):
                    useGt = False
                    useLt = True
                    curr = max(curr, j-i+1)
                    prev = arr[j]
                elif useLt and prev < arr[j]:
                    useLt = False
                    useGt = True
                    curr = max(curr, j-i+1)
                    prev = arr[j]
                else:
                    break
            # print(curr, j, useGt, useLt)
        return curr
            