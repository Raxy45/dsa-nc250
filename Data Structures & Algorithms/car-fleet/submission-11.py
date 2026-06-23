class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        updated_pos = list(zip(position, speed))
        updated_pos.sort()
        updated_pos = updated_pos[::-1]
        stk = []
        for current_car in updated_pos:
            position, speed = current_car
            req_time = (target-position)/speed
            # when you have array of time like [ 10, 2, 4.5, 2, 3, 3]
            # then your stk will be 3 -> not adding 3 (this 3 will always stand behind of 3)
            # 2 -> not adding 2, again it will stand behind of 3
            # 4.5 -> add this, this will stop others behind it and this will never reach fleet of 3
            # [4.5, 3]
            # 2 -> again dont add -> will join 4.5 fleet
            # 10 -> add -> will never reach 4.5 fleet -> and block other cars behind it

            # so when cur_time > stk[-1] -> only then add it. example for 4.5 and 10
            # for all others skip addition, except when stk is empty

            # note: key is the cars have to be arranged by their positions first and then begin from target[RHS to LHS]
            if not stk: 
                stk.append(req_time)
                continue

            if req_time > stk[-1]:
                stk.append(req_time)
            
        return len(stk)