class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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
    def combinationSumLoop(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        def dfs(req, temp):
            nonlocal ans
            print(req)
            if req==0: return temp

            for i in range(len(nums)):
                if (req-nums[i])<0: continue
                temp.append(nums[i])
                ans_array = dfs(req-nums[i], temp)
                if len(ans_array) > 0:
                    if tuple(ans_array) not in ans:
                        print('adding ans_array', ans_array, ans)
                        ans.add(tuple(ans_array))
                temp.pop()
            return []
        
        dfs(9, [])
        print(ans)
        return list(ans)
