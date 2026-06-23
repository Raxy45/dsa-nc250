class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum( numbers: List[int], target: int) -> List[int]:
            l, r = 0, len(numbers) - 1

            final_nums = []
            while l < r:
                curSum = numbers[l] + numbers[r]

                if curSum > target:
                    r -= 1
                elif curSum < target:
                    l += 1
                else:
                    final_nums.append([numbers[l], numbers[r]])
                    while l<r and numbers[l] == numbers[l+1]: l+= 1
                    while l<r and numbers[r] == numbers[r-1]: r-= 1
                l += 1
                r -= 1
            return final_nums

        nums.sort()
        ans = []
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                print('skipping')
                continue
            required_pair = twoSum(nums[i+1:], -nums[i])
            print(required_pair)
            if len(required_pair) > 0:
                for pair in required_pair:
                    pair.append(nums[i])
                    ans.append(pair)
        return ans