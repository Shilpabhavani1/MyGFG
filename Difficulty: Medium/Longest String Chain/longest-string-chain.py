#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        from collections import defaultdict
        
        s = set(words)
        ws = defaultdict(set)
        for w in words:
            for i in range(len(w)):
                e = w[:i] + w[i+1:]
                if e in s:
                    ws[w].add(e)

        words.sort(key=len)
        
        cache = defaultdict(int)
        
        def dfs(w):
            nonlocal cache
            r = 1
            for nbr in ws[w]:
                r = max(r, cache[nbr]+1)
            cache[w] = r
            return r
            
        ans = 0
        for w in words:
            ans = max(ans, dfs(w))
        return ans


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends