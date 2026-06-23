class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p, s in zip(position, speed)]

        stk = []
        print(pairs)
        print(sorted(pairs))
        print(sorted(pairs)[::-1])
        for p, s in sorted(pairs)[::-1]:
            stk.append((target-p)/s)
            if len(stk)>1 and stk[-1]<=stk[-2]:
                stk.pop()
        return len(stk)
        