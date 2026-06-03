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
                    if subsetSum==0: 
                        # Given the current state of used[], 
                        # letting nums[j] be the first element of the 
                        # new subset cannot lead to a solution.
                        
                        # We are starting a brand-new subset (subsetSum == 0).
                        #
                        # We chose nums[j] as the FIRST element of this subset and explored
                        # all possible continuations from that choice.
                        #
                        # If that entire subtree fails, then nums[j] cannot be the starting
                        # element of a valid subset in the current state.
                        #
                        # Since all empty subsets are equivalent (symmetry), there is no point
                        # trying nums[j] as the first element of another empty subset.
                        #
                        # Therefore we can prune and return False.
                        return False
            return False
        return dfs(0, k, 0)