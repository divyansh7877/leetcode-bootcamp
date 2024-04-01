class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        Using Queue.
        Uses Modulo 10^9 + 7
        '''
        mod = 10 ** 9  + 7
        q = deque([1] + [0] * (forget - 1))
        sharing = 0
        pre =  delay - 1
        
        for i in range(1, n): # For each day.
            sharing += q[pre] - q.pop() 
            q.appendleft(sharing % mod)
        
        result = sum(q) % mod
        return result