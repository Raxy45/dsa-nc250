class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start_p, end_p = 0, len(s)-1
        while start_p<=end_p:
            temp = s[end_p]
            s[end_p] = s[start_p]
            s[start_p] = temp
            start_p += 1
            end_p -= 1
        

        