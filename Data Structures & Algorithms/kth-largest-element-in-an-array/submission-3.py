class Solution:
    def get_pivot(self, nums, L, R):
        pivot = nums[L]
        i = L + 1
        j = R
        while i<=j:
            if nums[i] < pivot and nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] >= pivot: i += 1
            if nums[j] <= pivot: j -=1
        
        nums[L], nums[j] = nums[j], nums[L]
        return j

    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = self.get_pivot(nums, left, right)
            if pivot_index == k-1:
                return nums[pivot_index]
            elif pivot_index > k-1:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    def findKthLargestMaxHeap(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heapq.heappop(heap)

    def findKthLargestMinHeap(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        ans = -1
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return -ans