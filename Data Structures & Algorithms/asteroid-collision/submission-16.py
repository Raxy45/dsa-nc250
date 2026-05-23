class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            if a>0:
                stk.append(a)
                continue
            
            if not stk or stk[-1]<0:
                stk.append(a)
                continue
            
            add_a = True
            while stk and stk[-1] > 0:
                if (a+stk[-1]) == 0:
                    stk.pop()
                    add_a = False
                    break
                elif stk[-1] > abs(a):
                    add_a = False
                    break
                else:
                    stk.pop()
                    add_a = True
            if add_a:
                stk.append(a)
        return stk

















        stk = []
        for ast in asteroids:
            # print('current ast, stk', ast, stk)
            if ast > 0:
                stk.append(ast)
                continue
            
            # print('can collide')
            if not stk:
                # print('first ast')
                stk.append(ast)
                continue
            
            if stk[-1] < 0:
                # print('previous ast also in lhs direction')
                stk.append(ast)
                continue

            add_ast = False
            while stk and stk[-1]>0:
                # print('about to collide')
                popped_ast = stk.pop()
                collision = popped_ast + ast
                # print('popped ast and collision is', popped_ast, collision)
                if collision==0: 
                    # print('collision is 0 -> not adding')
                    add_ast = False
                    break
                if collision > 0:
                    stk.append(popped_ast)
                    add_ast = False
                    break
                add_ast = True
            if add_ast: stk.append(ast)
        return stk
