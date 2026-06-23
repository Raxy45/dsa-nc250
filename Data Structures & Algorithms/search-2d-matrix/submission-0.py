class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        r_m, c_m = R-1,C-1
        while r_m >= 0 and r_m<R:
            r_m = r_m//2
            # print('r_m, c_m', r_m, c_m)
            # print(matrix[r_m][0], matrix[r_m][C-1])
            if matrix[r_m][0]>target:
                r_m = r_m -1
            # elif matrix[r_m][0]>target:
            elif matrix[r_m][C-1]<target:
                r_m = r_m+1
            else:
                # This row has answer
                print('this row has answer')
                print(r_m, c_m)
                c_l = 0
                c_r = C-1
                count = 0
                while c_l<=c_r:
                    c_m = (c_l+c_r)//2
                    print('matrix[r_m][c_m]', matrix[r_m][c_m])
                    if matrix[r_m][c_m]==target:
                        return True
                    elif matrix[r_m][c_m]>target:
                        print('c_m>trgt')
                        c_r = c_m-1
                    else:
                        print('c_m<trgt')
                        c_l = c_m+1
                    # count += 1
                    # if count>5:
                    #     return 
                return False
        return False

