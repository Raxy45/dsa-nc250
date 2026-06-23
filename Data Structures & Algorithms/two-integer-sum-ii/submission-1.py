class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1
        ans = 0
        while i<j:
            ans = numbers[i] + numbers[j]
            if ans == target:
                return [i+1, j+1]
            
            if ans < target:
                i += 1
            elif ans > target:
                j -= 1
        