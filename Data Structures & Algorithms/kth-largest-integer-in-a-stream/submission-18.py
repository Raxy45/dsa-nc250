class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.sorted_nums) == 0:
            self.sorted_nums.append(val)
            return self.sorted_nums[0]
        if val < self.sorted_nums[0] : return self.sorted_nums[0]
        self.sorted_nums.append(val)
        self.sorted_nums = sorted(self.sorted_nums)[-self.k:]
        return self.sorted_nums[0]
        
