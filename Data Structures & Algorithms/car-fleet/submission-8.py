class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        updated_pos = list(zip(position, speed))
        updated_pos.sort()
        updated_pos = updated_pos[::-1]
        stk = []
        for current_car in updated_pos:
            position, speed = current_car
            req_time = (target-position)/speed
            if not stk: 
                stk.append(req_time)
                continue

            if req_time > stk[-1]:
                stk.append(req_time)
            
        return len(stk)