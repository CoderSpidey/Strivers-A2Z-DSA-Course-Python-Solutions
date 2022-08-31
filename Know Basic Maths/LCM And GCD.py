#User function Template for python3

class Solution:
    def gcd(self,a,b):
        if a == 0:
            return b
        return self.gcd(b % a,a)
        
    def lcmAndGcd(self, A , B):
        # code here 
        g = self.gcd(A,B)
        l = (A*B)//g
        return [l,g]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends
