class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        check_array = ["qwertyuiop" , "asdfghjkl" , "zxcvbnm" ]
        check_dict = {}
        result = [] 

        for key in check_array:
            check_dict[key] = len(key)

        for word in words:
            the_word = set(list(word.lower()))

            for key in check_dict:
                if len(set(list(key)).union(the_word)) == check_dict[key]:
                    result.append(word)
                
        return result

        