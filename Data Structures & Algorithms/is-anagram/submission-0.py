class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for i in s:
            s_map[i] = s_map.get(i, 0) + 1
        
        for i in t:
            s_map[i] = s_map.get(i, 0) - 1
        
        for alpha in s_map:
            if s_map[alpha]!=0:
                return False
        return True


        # for count in s_map:
        #     if(s_map[count != t_mapcount]):
        #         return False
        # return True
        