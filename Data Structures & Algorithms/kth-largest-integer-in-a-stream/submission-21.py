class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        i = len(nums)-1
        self.nums = []
        while k > 0:
            self.nums.append(nums[i])
            i -= 1
            k -= 1
        self.kth = self.nums[-1]
        print(self.nums)

    def add(self, val: int) -> int:
        if val > self.kth:
            old_kth = self.nums.pop()
            self.nums.append(val)
            self.nums.sort()
            self.nums = self.nums[::-1]
            self.kth = self.nums[-1]
        return self.kth
        
