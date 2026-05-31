class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(idx, temp):
            nonlocal ans
            # print(idx, temp, ans)
            if idx==len(nums):
                # print('adding temp', temp, 'to ans', ans)
                ans.append(temp.copy())
                # print('ans post',)
                return
            
            temp.append(nums[idx])
            dfs(idx+1, temp)

            temp.pop()
            # print('came back at idx call', idx, 'updated temp', temp)
            dfs(idx+1, temp)
        
        dfs(0, [])
        return ans
        