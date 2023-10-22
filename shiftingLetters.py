class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        cumultiveShifts = []

        for _ in range(len(s)+1):
            cumultiveShifts.append(0)
        
        for start, end, mid in shifts:
            if mid == 0:
                cumultiveShifts[start] -= 1
                cumultiveShifts[end+1] += 1
            else:
                cumultiveShifts[start] += 1
                cumultiveShifts[end+1] -= 1
        
        Sum = 0
        for i in range(len(s)):
            Sum += cumultiveShifts[i]
            
            newLetter = (((ord(s[i]) - 97) + Sum) % 26) + 97
            s = s[:i] + chr(newLetter) + s[i+1:]
        
        return s


        
