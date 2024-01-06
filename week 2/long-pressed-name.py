class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr = 0
        count = 0
        
        for idx in range(len(name)):
            # print(name[idx])
            if idx > 0 and name[idx] == name[idx - 1]:
                count -= 1
                if count == 0:
                    return False
                continue

            if ptr == len(typed) or typed[ptr] != name[idx]:
                return False
            
            count = 0
            while ptr < len(typed) and typed[ptr] == name[idx]:
                ptr += 1
                count += 1

        return False if ptr < len(typed) else True
