class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-k:]
        self.kth = None
        if self.nums:
            self.kth = self.nums[0]
        print(self.kth)


    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)
        if val < self.nums[0]:
            return self.nums[0]
        print('adding val', val, 'to', self.nums)
        self.nums.append(val)
        self.nums.sort()
        self.nums = self.nums[-self.k:]
        self.kth = self.nums[0]
        return self.kth
        

