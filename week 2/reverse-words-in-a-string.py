class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        lis = s.split()
        array = []

        for word in lis:
            array.append(word.strip())

        return ' '.join(array[::-1])




        