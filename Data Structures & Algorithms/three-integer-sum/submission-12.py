class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum( numbers: List[int], target: int) -> List[int]:
            l, r = 0, len(numbers) - 1

            while l < r:
                curSum = numbers[l] + numbers[r]

                if curSum > target:
                    r -= 1
                elif curSum < target:
                    l += 1
                else:
                    return [numbers[l], numbers[r]]
            return []

        nums.sort()
        ans = []
        print(nums)
        for i in range(len(nums)):
            required_pair = twoSum(nums[i+1:], -nums[i])
            if len(required_pair) > 0:
                print(required_pair)
                required_pair.append(nums[i])
                ans.append(required_pair)
        return ans