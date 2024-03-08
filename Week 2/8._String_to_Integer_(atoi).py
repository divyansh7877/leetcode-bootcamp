class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        Used String strip function, isdigit function and pow functions
        '''
        
        s=s.strip()
        if not s:
            return 0
        num=0
        neg=1
        i=0
        if s[0]=='-':
            neg=-1
            i=1
        elif s[0]=='+':
            i=1

        while i<len(s) and s[i].isdigit():
            d=int(s[i])
            num=num* 10 + d
            i+=1

            if num * neg  > pow(2, 31) - 1:
                return pow(2, 31) - 1
            
            if num * neg < -pow(2, 31) :
                return -pow(2, 31)

        return num * neg
        