class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.sorted_nums_from_k = self.get_sorted_nums(self.nums)[-k:]

    def get_sorted_nums(self, nums_till_k):
        print(sorted(nums_till_k))
        return sorted(nums_till_k)

    def add(self, val: int) -> int:
        if val < self.sorted_nums_from_k[0]:
            return self.sorted_nums_from_k[0]
        else:
            self.nums.append(val)
            self.sorted_nums_from_k = self.get_sorted_nums(self.nums[-self.k:])
            return self.sorted_nums_from_k[0]

            

