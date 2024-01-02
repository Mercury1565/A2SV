class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        ptr = len(processorTime) - 1
        result = 0

        for i in range(3 , len(tasks) , 4):
            print(i)
            result = max(result , processorTime[ptr] + tasks[i])
            ptr -= 1
        return result

        