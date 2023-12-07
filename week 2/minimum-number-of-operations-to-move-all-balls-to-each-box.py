class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        steps = []
        for i in range(len(boxes)):
            step = 0
            for j in range(len(boxes)):
                if j == i:
                    continue
                
                if boxes[j] == '1':
                    step += abs(i - j)

            steps.append(step)
        return steps

            

        