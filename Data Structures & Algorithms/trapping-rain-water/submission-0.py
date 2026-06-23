class Solution:
    def trap(self, height: List[int]) -> int:
        w_sum = 0
        i, j = 0, 1
        while i < len(height)-1:
            if height[i] == 0:
                i+= 1
                continue
            j = i + 1
            c_sum = 0
            while(j<len(height) and height[j]<height[i]):
                # c_sum += height[i] - height[j]
                j += 1
            
            if j<len(height) and height[i]<=height[j]:
                min_col = min(height[i], height[j])
                c_sum = 0
                print('min_col: ', min_col)
                for k in range(i+1, j):
                    print('current k', k, 'element ', height[k])
                    c_sum += abs(min_col - height[k])
                    print('c_sum ', c_sum)
                w_sum += c_sum
                print('w_sum: ', w_sum)
                i = j
            else:
                i += 1
        return w_sum

            