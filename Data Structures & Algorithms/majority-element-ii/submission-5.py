class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val1 = val2 = 0
        c1 = c2 = 0
        for i in nums:
            if i==val1:
                c1 += 1
            elif i==val2:
                c2 += 1
            elif c1==0:
                val1=i
                c1 = 1
            elif c2==0:
                val2=i
                c2=1
            else:
                c1 -= 1
                c2 -= 1

        tally_c1, tally_c2 = 0, 0
        for i in nums:
            if i==val1:
                tally_c1+= 1
            elif i==val2:
                tally_c2 += 1
        
        ans =[]
        if tally_c1 > len(nums)//3:
            ans.append(val1)

        if tally_c2 > len(nums)//3:
            ans.append(val2)

        return ans
        n = len(nums)
        num1 = num2 = -1
        cnt1 = cnt2 = 0

        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1
            elif cnt1 == 0:
                cnt1 = 1
                num1 = num
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == num1:
                cnt1 += 1
            elif num == num2:
                cnt2 += 1

        res = []
        if cnt1 > n // 3:
            res.append(num1)
        if cnt2 > n // 3:
            res.append(num2)

        return res
