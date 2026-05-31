class Solution:
    def combinationSum2Loop(self, nums, target):
        nums.sort()
        ans = []
        subset = []

        def dfs(start, remain):
            if remain == 0:
                ans.append(subset.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                if nums[i] > remain:
                    break

                subset.append(nums[i])
                dfs(i + 1, remain - nums[i])
                subset.pop()

        dfs(0, target)
        return ans

    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # TC: n log n + 2^(t/min(nums))

        # SC is 2^(t/min(nums))
        ans = []
        subset = []
        nums.sort()
        def dfs(req, idx):
            nonlocal ans
            if req==0:
                ans.append(subset.copy())
                return
            
            if idx == len(nums) or req < 0:
                return

            # Why don't we skip duplicates before the pick branch?
            #
            # Example:
            # nums = [1,2,2,2,5,7,8]
            #
            # Combination Sum II allows using each INDEX at most once,
            # not each VALUE at most once.
            #
            # Therefore combinations such as:
            # [2]
            # [2,2]
            # [2,2,2]
            # are valid because they use different indices.
            #
            # If we skipped duplicates here and jumped directly to the
            # last 2, we would lose combinations that require multiple
            # copies of 2.
            #
            # Hence we must first explore all combinations that include
            # the current 2.

            subset.append(nums[idx])
            dfs(req - nums[idx], idx + 1)
            subset.pop()

            # At this point, every combination that starts by taking
            # the current value (2) has already been explored.
            #
            # Now we want the "don't take 2" branch.
            #
            # If we simply did:
            # dfs(req, idx + 1)
            #
            # then we'd start again from another 2 and generate the
            # same combinations multiple times.
            #
            # Therefore, for the NOT-PICK branch, skip all duplicates
            # and move directly to the next distinct value.

            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(req, idx+1)
        dfs(target, 0)
        return ans