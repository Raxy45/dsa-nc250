class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        min_boat = 0
        while l <= r:
            if people[l]+people[r] > limit:
                r -= 1
                min_boat += 1
                # to heavy to go with someone
            elif people[l]+people[r] == limit:
                min_boat += 1
                l += 1
                r -= 1
                # perfect match
            elif people[l]+people[r]<limit:
                min_boat += 1
                l += 1
                r -= 1
        return min_boat
        
    def numRescueBoatsBasic(self, people: List[int], limit: int) -> int:
        min_boat = 0
        for i in range(0, len(people)-1):
            # print('current i: ', people[i])
            if people[i]==-1:
                continue
            req_wt = limit - people[i]
            wt_found = False
            best_person_index = -1
            min_wt_diff = sys.maxsize
            for j in range(i+1, len(people)):
                if people[j] == -1:
                    continue
                if req_wt >= people[j]:
                    curr_wt_diff = req_wt - people[j]
                    if curr_wt_diff < min_wt_diff:
                        min_wt_diff = curr_wt_diff
                        best_person_index = j
                    # min_boat += 1
                    # print('found')
                    # print(people[i], people[j])
                    # print('curr wt diff: ', curr_wt_diff)
                    # print('min wt diff: ', min_wt_diff)
                    # print('min_boat: ', min_boat)
                    # people[j] = -1
                    wt_found = True
            if wt_found:
                # print('ideal match: ')
                # print(people[i], people[j])
                people[best_person_index] = -1
            min_boat += 1
            # print('min_boat outside: ', min_boat)
            # print('people: ', people)
            # print('*'*30)
        if people[len(people)-1] <= limit and people[len(people)-1]!=-1:
            min_boat += 1
        return min_boat