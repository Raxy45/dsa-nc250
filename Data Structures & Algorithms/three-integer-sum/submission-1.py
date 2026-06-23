class Solution:
    def canonical_triplet(self, triplet):
        # generate all rotations
        rotations = [
            triplet,
            (triplet[1], triplet[2], triplet[0]),
            (triplet[2], triplet[0], triplet[1])
        ]
        # return the lexicographically smallest rotation
        return min(rotations)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet = self.canonical_triplet((nums[i],nums[j],nums[k]))
                        print(triplet)
                        if triplet not in ans:
                            ans[triplet] = [nums[i], nums[j], nums[k]]
        return list(ans.values())