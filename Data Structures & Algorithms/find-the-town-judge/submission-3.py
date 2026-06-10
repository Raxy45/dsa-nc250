class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(list)
        outgoing = defaultdict(list)
        for person, trustworthy_person in trust:
            incoming[trustworthy_person].append(person)
            outgoing[person].append(trustworthy_person)

        print(incoming)
        print(outgoing)
        for i in range(1, n+1):
            # print(i in outgoing, len)
            if i not in outgoing and len(incoming[i])==n-1:
                return i
                # person trusts no body -> not in outgoing
                # person is been trusted by all except him/her -> n-1
        return -1

        