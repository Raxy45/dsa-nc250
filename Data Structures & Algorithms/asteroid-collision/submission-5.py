class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if len(stack)==0:
                stack.append(a)
                continue
            
            add_a = True
            while a<0 and len(stack)>0 and stack[-1]>0:
                if stack[-1]==abs(a):
                    stack.pop()
                    add_a = False
                    break
                
                if stack[-1]>abs(a):
                    add_a = False
                    break
                stack.pop()
                add_a = True
            
            if add_a:
                stack.append(a)
        return stack

        #     if a > 0:
        #         stack.append(a)
        #     else:
        #         add_ast = True
        #         while len(stack)>0 and a < 0 and stack[-1] > 0:
        #             diff = a + stack[-1]
        #             # print('diff ', diff, a, stack[-1])
        #             # print(stack)
        #             if diff < 0:
        #                 add_ast = True
        #                 stack.pop()
        #             elif diff > 0:
        #                 add_ast = False
        #                 break
        #             else:
        #                 stack.pop()
        #                 add_ast = False
        #                 break
        #         # print(add_ast)
        #         if add_ast:
        #             stack.append(a)
        # return stack