class Solution:
    def lengthOfLIS(self, nums):
        ip = []
        def BS(num):
            l, r = 0, len(ip)-1
            print(ip, num)
            if len(ip)==0:
                ip.append(num)
                return
            if len(ip)>0:
                if num>ip[-1]:
                    print('adding num to ip', num, ip)
                    ip.append(num)
                    return

            while l<=r:
                mid = (l+r)//2
                if ip[mid] == num:
                    return
                if num<ip[mid]:
                    r=mid-1
                    # print('mid gt than num', ip[mid], num)
                else:
                    # print('mid')
                    l = mid+1
            print(l, r, num)
            ip[l] = num
        for num in nums:
            BS(num)
        print(ip)
        return len(ip)
            
    def lengthOfLISBottomUP(self, nums):
        dp = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
    def lengthOfLISTopDown(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        dp[len(nums)] = 0
        ans = 1
        def solve(idx):
            nonlocal ans
            if idx in dp:
                return dp[idx]
            
            res = 1
            for i in range(idx+1, len(nums)):
                if nums[i] > nums[idx]:
                    res = max(res, 1+solve(i))
            dp[idx] = res
            return dp[idx]
        for i in range(len(nums)):
            ans = max(ans, solve(i))
        return ans