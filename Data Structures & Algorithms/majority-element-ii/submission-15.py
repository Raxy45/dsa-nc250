class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums)==1:
            return [nums[0]]
        
        n1, n2 = nums[0], nums[1]
        c1, c2 = 0, 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
            
            if c1 == 0:
                n1 = num
            elif c2 == 0:
                n2 = num
        
        t_c1, t_c2 = 0, 0
        for num in nums:
            if num==n1:
                t_c1 += 1
            elif num == n2:
                t_c2 += 1
        
        ans=[]
        if t_c1>(len(nums)/3):
            ans.append(n1)
        if t_c2>(len(nums)/3):
            ans.append(n2)
        return ans