class Solution:
    def decodeString(self, s: str) -> str:
        # TC is O(n*k)
        # Where:
        #     n = length of input
        #     k = max decoded string expansion factor
        # Example: 1000[a] -> 1000*a -> takes time

        # OR
        # TC = O(m)
            # m = length of decoded output string.
            #
            # Each character is pushed/popped from the stack
            # a constant number of times, and string expansion
            # (char * count) contributes proportional to the
            # size of the generated output.

        # SC: O(m)
            #
            # Stack and final decoded string may store up to
            # the entire decoded output.
            #
            # Example:
            # "1000[a]" -> decoded string length = 1000
            # even though input length is only 7.
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)