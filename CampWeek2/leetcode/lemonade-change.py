class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashMap = {5:0 , 10:0}

        for bill in bills:
            payement = bill

            if payement == 20:
                if hashMap[10] >= 1:
                    hashMap[10] -= 1
                elif hashMap[5] >= 2:
                    hashMap[5] -= 2
                else:
                    return False
                payement -= 10

            if payement == 5:
                hashMap[5] += 1
                continue
            elif payement == 10:
                if hashMap[5] == 0:
                    return False
                hashMap[5] -= 1
                if bill == 10:
                    hashMap[10] += 1

        return True

                