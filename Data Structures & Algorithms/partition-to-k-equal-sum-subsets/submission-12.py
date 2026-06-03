class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k>0: return False

        nums.sort(reverse=True)
        t = sum(nums)/k
        used = [False] * len(nums)
        def dfs(i, k, subsetSum):
            if k==0:
                return True
            if subsetSum==t:
                # you are starting new subset, therefore you can start from 0th index
                return dfs(0, k-1, 0)

            for j in range(i, len(nums)):
                if (subsetSum+nums[j]) <= t and not used[j]:
                    used[j] = True
                    if dfs(j+1, k, subsetSum+nums[j]):
                        return True
                    used[j] = False
                    if subsetSum==0: return False
            return False
        return dfs(0, k, 0)