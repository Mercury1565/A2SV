class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        result = []

        for path in paths:
            first_space = path.index(" ")
            folder = path[ : first_space]
            files = path[first_space + 1 : ].split()

            for file in files:
                content = file[file.index('(') + 1 : -1]
                dic[content].append(folder + '/' + file[ : file.index('(')])


        for key in dic:
            if len(dic[key]) > 1:
                result.append(dic[key])

        return result
        