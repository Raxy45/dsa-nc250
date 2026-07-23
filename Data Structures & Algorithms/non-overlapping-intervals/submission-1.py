class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
                # Why prevEnd = min(prevEnd, end)?
                    #
                    # Example:
                    #
                    # A: [1, 5]
                    # B:     [3, 4]
                    # C:         [4, 8]
                    #
                    # A overlaps B, so we must remove one.
                    #
                    # Keep A (end = 5):
                    # [1------5]
                    #      [3-4]
                    #         [4------8]
                    # => A also overlaps C (5 > 4)
                    #
                    # Keep B (end = 4):
                    # [1------5]
                    #      [3-4]
                    #         [4------8]
                    # => B does NOT overlap C (4 <= 4)
                    #
                    # Therefore, when two intervals overlap, keep the one that ends earlier
                    # (smaller end), as it leaves more room for future intervals.
                    #
                    # prevEnd = min(prevEnd, end)

        return res