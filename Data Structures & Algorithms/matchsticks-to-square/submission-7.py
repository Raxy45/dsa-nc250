class Solution:
    def makesquare(self, mtk: List[int]) -> bool:
        sides_sum = sum(mtk)
        max_side = max(mtk)
        if (sides_sum)%4 > 0: return False

        side_len = sides_sum/4
        if max_side>side_len: return False

        sides, subset = [], []
        k = 0
        def dfs(req, n_sides):
            nonlocal k, subset
            if k>20: return False
            print('Current req', req, 'sides comp', sides)
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
                subset.pop()
                mtk[i] = temp
            k += 1
            return False
        return dfs(side_len, 0)

                

                        