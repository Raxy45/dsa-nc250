class Solution:
    def lengthOfLIS(self, nums):
        temp = []

        for num in nums:
            idx = self.binary_search(temp, num)

            if idx == len(temp):
                temp.append(num)
            else:
                temp[idx] = num

        return len(temp)

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left   # insertion position (lower_bound)

class SolutionBottomUPME:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[len(nums)-1] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], 1+dp[i])
        return max(dp)
class SolutionRecMemo:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def solve(i):
            if i in dp:
                return dp[i]

            res = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    res = max(res, 1 + solve(j))

            dp[i] = res
            return res

        ans = 0
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans