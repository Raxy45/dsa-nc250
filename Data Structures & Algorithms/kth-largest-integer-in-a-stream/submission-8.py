class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        print(self.nums)
        self.k_th = self.nums[-k] if len(nums) > 0 else float('-inf')
        self.sorted_from_k = self.nums[-k:] if k > 0 else []
        print(self.sorted_from_k)

    def add(self, val: int) -> int:
        if val<self.k_th: return self.k_th

        self.sorted_from_k.append(val)
        self.sorted_from_k.sort()
        self.sorted_from_k = self.sorted_from_k[1:]
        self.k_th = self.sorted_from_k[0]
        return self.k_th

