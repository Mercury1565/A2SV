class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ssum = skill[0] + skill[-1]
        chemistry = 0
        
        right = len(skill) - 1

        for left in range(len(skill) // 2):
            if skill[left] + skill[right] == ssum:
                chemistry += (skill[left] * skill[right])
            else:
                return -1
            right -= 1
        return chemistry



        