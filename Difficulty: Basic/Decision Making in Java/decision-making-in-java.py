
class Solution:
    def compareNM(self, n : int, m : int) -> str:
        # code here
        if n<m:
            return "lesser"
        if n==m:
            return "equal"
        else:
            return "greater"
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        obj = Solution()
        res = obj.compareNM(n, m)
        
        print(res)
        

        print("~")
# } Driver Code Ends