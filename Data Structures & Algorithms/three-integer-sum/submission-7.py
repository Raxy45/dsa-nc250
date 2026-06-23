class Solution:
    def canonical_triplet_set(self, triplet):
    # sort the elements and return as a tuple (hashable)
        return tuple(sorted(triplet))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        a = []
        def twoSum(l,r, current_index):
            target = -sorted_nums[current_index]
            print('target', target)
            while l < r:
                c_sum = sorted_nums[l]+sorted_nums[r]
                if c_sum==target:
                    a.append([sorted_nums[current_index], sorted_nums[l], sorted_nums[r]])
                    l+=1
                    r-=1
                    while l < r and sorted_nums[l]==sorted_nums[l-1]:
                        l+= 1
                    while l < r and sorted_nums[r]==sorted_nums[r+1]:
                        r-=1
                elif c_sum > target:
                    r -= 1
                else:
                    l += 1
        print('sorted nums', sorted_nums)
        for i in range(0, len(nums)-2):
            if i > 0 and sorted_nums[i]!=sorted_nums[i-1]:
                twoSum(i+1, len(nums)-1, i)
            if i == 0:
                twoSum(i+1, len(nums)-1, i)
        print(a)
        return a
                    