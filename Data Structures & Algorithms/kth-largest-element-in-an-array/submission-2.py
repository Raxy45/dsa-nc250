class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap)>k:
                heapq.heappop(heap)
            print('heap', heap)
        print(heap)
        return heapq.heappop(heap)

    def findKthLargestMinHeap(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        ans = -1
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return -ans