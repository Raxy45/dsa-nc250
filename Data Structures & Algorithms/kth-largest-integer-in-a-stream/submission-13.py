class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        print(self.nums)
        self.k_th = self.nums[-k] if len(nums) > 0  and k < len(nums) else float('inf')
        self.sorted_from_k = self.nums[-k:] if k > 0 else []
        print(self.sorted_from_k)

    def add(self, val: int) -> int:
        if len(self.nums)>0 and val<self.k_th: return self.k_th

        self.sorted_from_k.append(val)
        self.sorted_from_k.sort()
        self.sorted_from_k = self.sorted_from_k[1:] if len(self.sorted_from_k) > 1 else self.sorted_from_k
        self.k_th = self.sorted_from_k[0]
        return self.k_th if self.k_th!=float('inf') else 0