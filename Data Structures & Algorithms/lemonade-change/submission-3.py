from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0

        for b in bills:
            if b == 5:
                five += 1

            if b == 10:
                ten += 1

            change = b - 5

            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False

            elif change == 15:
                if five > 0 and ten > 0:
                    five, ten = five - 1, ten - 1
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
