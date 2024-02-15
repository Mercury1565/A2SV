class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers) 
        inputs = [0] * n
        for c in range(len(customers)):
            if customers[c]=='Y':
                inputs[c] = 1
         
        prefix = [0] * (n+1)
        postfix = [0] * (n+1)
        postfix[-2] = inputs[-1]
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] + inputs[i]
        
        prefix[1] = 1 if inputs[0] == 0 else 0
        for i in range(2,n+1):
            if inputs[i - 1] == 0:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        value = inf
        for i in range(len(prefix)):
            if postfix[i] + prefix[i] < value:
                value = postfix[i] + prefix[i]
                idx = i

        return idx

        