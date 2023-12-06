class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        def find_common_strings(list1 , list2):
            dic = {}
            index_sum = set()

            for i in range(len(list1)):
                
                if list1[i] in list2:
                    ssum = i + list2.index(list1[i])
                    index_sum.add(ssum)
                    if ssum not in dic: 
                        dic[ssum] = [list1[i]]
                    else:
                        dic[ssum].append(list1[i])

            return dic[min(index_sum)]

    
        if len(list1) <= len(list2):
            return find_common_strings(list1 , list2)
        return find_common_strings(list2 , list1)
        

    