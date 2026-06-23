class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if m < n:
            return False

        # Frequency arrays for characters a-z
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Build frequency for s1 and first window in s2
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Sliding window over s2
        left = 0
        for right in range(n, m):
            # Check if current window matches
            if s1_count == s2_count:
                return True

            # Slide the window forward by removing left char
            s2_count[ord(s2[left]) - ord('a')] -= 1
            left += 1

            # Add the new character entering the window
            s2_count[ord(s2[right]) - ord('a')] += 1

        # Check the last window
        return s1_count == s2_count
