class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        ans = 0
        while l<=r:
            c_wt = people[l] + people[r]
            if c_wt <= limit:
                ans += 1
                l += 1
                r -= 1
            elif c_wt>limit:
                ans += 1 
                r -= 1
        return ans




        l, r = 0, len(people)-1
        people.sort()
        ans = 0
        while l<=r:
            if (people[l]+people[r]) <= limit:
                ans += 1
                l += 1
                r -= 1
            else:
                r -= 1
                ans += 1
        return ans