class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        ans = float('inf')
        def get_partition_count(allowed_sum):
            print('finding partitions for', allowed_sum)
            p_count = 0
            curr = 0
            for n in nums:
                curr += n
                if curr==allowed_sum:
                    curr = 0
                    p_count += 1
                elif curr>allowed_sum:
                    curr = n
                    p_count += 1
            if curr>0:
                p_count += 1
            return p_count

        while l<=r:
            curr_sum = (l+r)//2
            partitions = get_partition_count(curr_sum)
            # print('partitions', partitions, mx_sum)
            if partitions > k:
                l = curr_sum + 1
            else:
                r = curr_sum - 1
                ans = min(ans, curr_sum)
        return ans
