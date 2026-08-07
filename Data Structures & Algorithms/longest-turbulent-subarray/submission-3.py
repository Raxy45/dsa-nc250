class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        # sign[i] represents comparison between arr[i] and arr[i-1]
        #  1 : arr[i] > arr[i-1]
        # -1 : arr[i] < arr[i-1]
        #  0 : arr[i] == arr[i-1]
        sign = [0] * n

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                sign[i] = 1
            elif arr[i] < arr[i - 1]:
                sign[i] = -1

        curr = 1
        ans = 1

        for i in range(1, n):

            # Equal elements -> turbulence breaks completely
            if sign[i] == 0:
                curr = 1

            # Sign alternates (+,-) or (-,+)
            elif sign[i] != sign[i - 1]:
                curr += 1

            # Same sign (+,+) or (-,-)
            # Current pair itself forms a turbulent subarray of length 2
            else:
                curr = 2

            ans = max(ans, curr)

        return ans


    def maxTurbulenceSizeN2(self, arr: List[int]) -> int:
        # create new temporary arry, holds tuple of (prevGT, prevLt) -> (1,0), (0,1), (0,)
        # Iterate over array, compute this array values
        # now in next loop, iterate over and find out the max when either prevGt is alternating or prevLt is alternating, when the sign no longer alternates -> curr = max(curr, curr_idx- idx ) ,bring idx to curr_idx
        curr = 1
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
            