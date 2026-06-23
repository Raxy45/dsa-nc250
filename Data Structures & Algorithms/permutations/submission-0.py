class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return [[]]


        current_perm = self.permute(nums[1:])
        current_result = []
        for p in current_perm:
            temp = []
            for i in range(len(p)+1):
                temp = p.copy()
                temp.insert(i, nums[0])
                current_result.append(temp)
        return current_result

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        print('perms ', perms, 'for ', nums[1:])
        res = []
        for p in perms:
            print('going in perms for', perms)
            print(len(p)+1)
            for i in range(len(p) + 1):
                print('inserting i', i)
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
                print(res)
        print('result for perms', nums[1:])
        return res