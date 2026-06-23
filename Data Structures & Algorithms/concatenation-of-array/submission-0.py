class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in nums:
            new_list.append(i)
        for i in nums:
            new_list.append(i)
        return new_list
        