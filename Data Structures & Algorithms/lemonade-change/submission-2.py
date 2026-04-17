class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1

            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True
class SolutionME:
    def lemonadeChange(self, bills: List[int]) -> bool:
        wallet = {
            5: 0, 10: 0, 20: 0
        }
        for bill in bills:
            # print('i')
            req_change = bill - 5
            # change -> check if this change exists in wallet
            for coin in [20, 10, 5]:
                while wallet[coin] > 0 and coin<=req_change:
                    req_change -= coin
                    wallet[coin] -= 1
            if req_change==0:
                wallet[bill] += 1
            else:
                return False
        return True
