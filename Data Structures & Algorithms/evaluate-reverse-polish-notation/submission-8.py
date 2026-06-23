class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print('i ', i)
            print(stack)

            if i == '+':
                last = int(stack.pop())
                second_last = int(stack.pop())
                print('last, second last ', last, second_last)
                resultant = last + second_last
                stack.append(resultant)
            elif i == '-':
                last = int(stack.pop())
                second_last = int(stack.pop())
                print('last, second last ', last, second_last)
                resultant = second_last - last
                stack.append(resultant)
            elif i == '*':
                last = int(stack.pop())
                second_last = int(stack.pop())
                print('last, second last ', last, second_last)
                resultant = last * second_last
                stack.append(resultant)
            elif i == '/':
                last = int(stack.pop())
                second_last = int(stack.pop())
                print('last, second last ', last, second_last)
                resultant = last // second_last
                stack.append(resultant)
            else:
                stack.append(int(i))
        return int(stack.pop())