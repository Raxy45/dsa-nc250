class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        l, r = 0, len(people)-1
        while l<=r:
            current_wt = people[l] + people[r]
            if current_wt <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            ans += 1
        return ans
                