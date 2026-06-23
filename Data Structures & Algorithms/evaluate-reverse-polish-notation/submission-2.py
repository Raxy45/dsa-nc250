class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print('i ', i)
            print(stack)
            if i == '+':
                last = int(stack.pop())
                second_last = int(stack.pop())
                resultant = last + second_last
                stack.append(resultant)
            elif i == '-':
                last = int(stack.pop())
                second_last = int(stack.pop())
                resultant = last - second_last
                stack.append(resultant)
            elif i == '*':
                last = int(stack.pop())
                second_last = int(stack.pop())
                resultant = last * second_last
                stack.append(resultant)
            elif i == '/':
                last = int(stack.pop())
                second_last = int(stack.pop())
                resultant = int(last / second_last)
                stack.append(resultant)
            else:
                stack.append(i)
        return int(stack.pop())