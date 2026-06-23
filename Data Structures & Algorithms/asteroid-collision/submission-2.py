class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                add_ast = True
                while len(stack)>0 and a < 0 and stack[-1] > 0:
                    diff = a + stack[-1]
                    # print('diff ', diff, a, stack[-1])
                    # print(stack)
                    if diff < 0:
                        add_ast = True
                        stack.pop()
                    elif diff > 0:
                        add_ast = False
                        break
                    else:
                        stack.pop()
                        add_ast = False
                        break
                # print(add_ast)
                if add_ast:
                    stack.append(a)
        return stack