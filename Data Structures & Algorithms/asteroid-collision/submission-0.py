class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if a > 0:
                stack.append(a)
            else:
                add_ast = True
                while stack and a < 0 and stack[-1] > 0:
                    diff = a + stack[-1]
                    if diff < 0:
                        add_ast = True
                        stack.pop()
                    elif diff > 0:
                        a = 0
                        asteroid_add = False
                    else:
                        a = 0
                        stack.pop()
                        asteroid_add = False
                if add_ast:
                    stack.append(a)
        return stack