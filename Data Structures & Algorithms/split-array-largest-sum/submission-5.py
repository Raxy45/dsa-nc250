class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)

        def get_partition_count(rsum):
            curr = 0
            csum = 0
            for n in nums:
                csum += n
                if csum == rsum:
                    curr += 1
                    csum = 0
                    continue
                if csum < rsum:
                    continue
                
                # csum > rsum 
                curr += 1
                csum = n
            if csum > 0:
                curr += 1
            return curr
        while l<=r:
            req_sum = (l+r)//2
            print('l and r', l, r)
            current_partition_count = get_partition_count(req_sum)
            print(current_partition_count, 'for', req_sum)
            if current_partition_count > k:
                l = req_sum + 1
            else:
                # cpc <= k -> scope for lowering the weight
                r = req_sum - 1
            print('updated l  and r', l, r)
        return l