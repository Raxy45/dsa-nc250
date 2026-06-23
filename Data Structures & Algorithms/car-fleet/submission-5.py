class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p, s in zip(position, speed)]

        stk = []
        print(pairs)
        print(sorted(pairs))
        print(sorted(pairs)[::-1])
        for p, s in sorted(pairs)[::-1]:
            cur_time = (target-p)/s
            print('cur_time', cur_time)
            if stk and cur_time > stk[-1]:
                stk.append(cur_time)
            elif len(stk) == 0:
                stk.append(cur_time)
        return len(stk)
        for p, s in sorted(pairs)[::-1]:
            cur_time = (target-p)/s
            print('cur_time', cur_time)
            if len(stk)>0:
                if cur_time==stk[-1]:
                    # when you have cur=time as 3 and stk[-1] is 3, you can pop this
                    # you only need to keep one count of 3
                    stk.pop()
                elif cur_time<stk[-1]:
                    # this cur_time car will have to stand behind slower one stk[1]
                    continue
            # when stk is empty add curr_time -> easy
            # when cur_time say 15, stk[-1]=10, then will add this, as
            # car with 15 second does not have wait for 10, this will eventually come after 
            # 5 second.

            # stk structure is 5,10,15 
            stk.append(cur_time)
            print('final stk', stk)
        return len(stk)
        #     stk.append((target-p)/s)
        #     if len(stk)>1 and stk[-1]<=stk[-2]:
        #         stk.pop()
        # return len(stk)
        