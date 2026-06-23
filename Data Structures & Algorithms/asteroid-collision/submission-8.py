class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            print('current ast, stk', ast, stk)
            if ast > 0:
                stk.append(ast)
                continue
            
            print('can collide')
            if not stk:
                print('first ast')
                stk.append(ast)
                continue
            
            if stk[-1] < 0:
                print('previous ast also in lhs direction')
                stk.append(ast)
                continue

            while stk:
                print('about to collide')
                popped_ast = stk.pop()
                collision = popped_ast + ast
                print('popped ast and collision is', popped_ast, collision)
                if collision==0: 
                    print('collision is 0 -> not adding')
                    break
                if collision > 0:
                    stk.append(popped_ast)
                    break

        return stk
