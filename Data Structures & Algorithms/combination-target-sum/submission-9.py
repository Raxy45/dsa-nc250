class Solution:
    def combinationSumRec(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(idx, req, temp):
            if req==0:
                return temp
            if idx==len(nums) or req<0:
                return []

            temp.append(nums[idx])
            ans_arr = dfs(idx, req-nums[idx], temp)
            if len(ans_arr)>0:
                ans.append(ans_arr.copy())
            
            temp.pop()
            ans_arr = dfs(idx+1,req, temp)
            if len(ans_arr)>0:
                ans.append(ans_arr.copy())
            return []
            
        dfs(0, target, [])
        return ans
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(idx, req, temp):
            nonlocal ans
            print(req)
            if req==0: return temp

            for i in range(idx, len(nums)):
                if (req-nums[i])<0: continue
                temp.append(nums[i])
                ans_array = dfs(i, req-nums[i], temp)
                if len(ans_array) > 0:
                    ans.append(ans_array.copy())
                temp.pop()
            return []
        
        dfs(0, target, [])
        print(ans)
        return list(ans)
