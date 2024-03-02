class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        result = 0
        for i in range(length-1,-1,-1):
            result+= digits[i]*(10**((length-1)-i))
        result+=1

        output = [int(x) for x in str(result)]
        return output