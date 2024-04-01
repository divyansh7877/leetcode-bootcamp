class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Using stack
        '''
        my_stack = []
        for chr in s:
            if chr == "]":
                val = my_stack.pop()
                item = ""
                
                while my_stack and not str(val).isnumeric():
                    
                    item = val + item if val != "[" else item
                    val = my_stack.pop()

                number = val
                while my_stack and str(my_stack[-1]).isnumeric():
                    number = my_stack.pop() + number
                
                for _ in range(int(number)):
                    my_stack.append(item)
        
            else:
                my_stack.append(chr)
        
        return "".join(my_stack)