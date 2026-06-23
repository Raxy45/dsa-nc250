class Solution:
    def canonical_triplet_set(self, triplet):
    # sort the elements and return as a tuple (hashable)
        return tuple(sorted(triplet))

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet = self.canonical_triplet_set((nums[i],nums[j],nums[k]))
                        print(triplet)
                        print('beforr', ans)
                        if triplet not in ans:
                            print('s')
                            ans[triplet] = [triplet[0], triplet[1], triplet[2]]
                        print('after', ans)
        return list(ans.values())