class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for idx in range(len(digits) - 1 , -1 , -1):
            if idx == len(digits) - 1:
                carry = 0
                if digits[idx] != 9:
                    digits[idx] += 1
                else:
                    digits[idx] -= 9
                    carry += 1
                continue

            if digits[idx] + carry < 10:
                digits[idx] += carry
                if carry != 0:
                    carry -= 1
            else:
                digits[idx] -= 9

        return digits if carry == 0 else [carry] + digits

            

                

            
        