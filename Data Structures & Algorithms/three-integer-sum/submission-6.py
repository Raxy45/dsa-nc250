class Solution:
    def canonical_triplet_set(self, triplet):
    # sort the elements and return as a tuple (hashable)
        return tuple(sorted(triplet))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        ans = {}
        def twoSum(l,r, current_index):
            target = -sorted_nums[current_index]
            print('target', target)
            while l < r:
                c_sum = sorted_nums[l]+sorted_nums[r]
                if c_sum==target:
                    triplet = tuple(sorted([sorted_nums[current_index], sorted_nums[l], sorted_nums[r]]))
                    if triplet not in ans:
                        ans[triplet] = list(triplet)
                    l += 1
                    r -= 1
                elif c_sum > target:
                    r -= 1
                else:
                    l += 1
        print('sorted nums', sorted_nums)
        for i in range(0, len(nums)-2):
            print('i', i)
            print('i+1', i+1)
            twoSum(i+1, len(nums)-1, i)
        print(ans.values())
        return list(ans.values())
                    