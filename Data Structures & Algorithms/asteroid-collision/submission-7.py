class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            if ast > 0:
                stk.append(ast)
                continue
            
            if not stk:
                stk.append(ast)
                continue
            
            add_ast = True
            while stk and stk[-1] > 0:
                curr_collision = stk[-1] + ast
                # print(stk)
                # print(ast)
                # print(curr_collision)
                if curr_collision== 0:
                    stk.pop()
                    add_ast = False
                    break
                elif curr_collision > 0:
                    add_ast = False
                    break
                stk.pop()
                # print('*'*30)
            if add_ast:
                stk.append(ast)
        return stk
                
            