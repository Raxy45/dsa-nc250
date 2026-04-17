class Solution:
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
                # print('bill', bill)
                # print(wallet)
                return False
        return True
