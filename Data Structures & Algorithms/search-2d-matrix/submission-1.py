class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        r_m, c_m = R-1,C-1
        r_l, r_r = 0, R-1
        c = 0
        while r_l<=r_r:
            r_m = (r_l+r_r)//2
            if c>10:
                return True
            
            print('r_m, c_m', r_m, c_m)
            print(matrix[r_m][0], matrix[r_m][C-1])
            if matrix[r_m][0]>target:
                print('upper row')
                r_r = r_m-1
            # elif matrix[r_m][0]>target:
            elif matrix[r_m][C-1]<target:
                print('before rm', r_m)
                r_l = r_m+1
                print(
                'after rm', r_m
                )
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
            c += 1
            # return True
        return False

