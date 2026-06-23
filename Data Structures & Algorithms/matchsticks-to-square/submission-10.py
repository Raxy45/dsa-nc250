class Solution:
    def makesquare(self, mtk: List[int]) -> bool:
        sides_sum = sum(mtk)
        max_side = max(mtk)
        if (sides_sum)%4 > 0: return False

        side_len = sides_sum/4
        if max_side>side_len: return False
        sides = [0] * 4

        def dfs(idx, subset):
            if idx==4:
                return True
            
            for i in range(len(mtk)):
                for side in range(4):
                    if (sides[side]+mtk[i]) > side_len or mtk[i] == float('inf'):
                        continue
                    
                    subset.append(mtk[i])
                    sides[side] += mtk[i]
                    temp = mtk[i]
                    mtk[i] = float('inf')
                    if sides[side] == side_len:
                        idx += 1
                    if dfs(idx, subset): return True

                    subset.pop()
                    sides[side] -= temp
                    mtk[i] = temp
                if sides[side] == 0:
                    return False
            return False
        return dfs(0, [])



    def makesquareMy(self, mtk: List[int]) -> bool:
        sides_sum = sum(mtk)
        max_side = max(mtk)
        if (sides_sum)%4 > 0: return False

        side_len = sides_sum/4
        if max_side>side_len: return False

        sides, subset = [], []
        k = 0
        print(max_side, side_len)
        def dfs(req, n_sides):
            nonlocal k, subset
            if k>20: return False
            print('Current req', req, 'sides comp', sides, subset)
            if req==0:
                print('adding subset to ans', subset, n_sides)
                sides.append(subset.copy())
                if n_sides==3:
                    return True
                subset = []
                return dfs(side_len, n_sides+1)
            
            curr = []
            for i in range(len(mtk)):
                if mtk[i]==float('inf') or mtk[i]>req:
                    continue
                subset.append(mtk[i])
                temp = mtk[i]
                mtk[i] = float('inf')

                if dfs(req-temp, n_sides):
                    return True
                # else:
                #     # This means, with given side we cant form any side of square!
                #     # example: [3,3,3,4]. Now with 3, you cant pair up anything and therefore
                #     # we can say we cant form square with this input straightaway! 
                #     return False
                if subset:
                    subset.pop()
                mtk[i] = temp
            k += 1
            return False
        return dfs(side_len, 0)

                

                        