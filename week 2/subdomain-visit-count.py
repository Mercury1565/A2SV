class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        answer = []

        for domain in cpdomains:
            rep = int(domain[ : domain.index(' ')])
            url = domain[domain.index(' ') + 1 :]
            arr = url.split('.')

            for i in range(len(arr)):
                temp = '.'.join(arr[i : ])
                dic[temp] += rep
            
        for key in dic:
            answer.append(str(dic[key]) + ' ' + key)
        return answer







        