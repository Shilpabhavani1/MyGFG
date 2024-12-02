#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        dp = [0]*len(pat)
        
        for i in range(1, len(pat)):
            j = dp[i-1]
            while j > 0 and pat[j] != pat[i]:
                j = dp[j-1]
            dp[i] = j + int(pat[j] == pat[i])
            
        i, j = 0, 0
        result = []
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == len(pat):
                    result.append(i-j)
                    j = dp[j-1]
            else:
                if j > 0:
                    j = dp[j-1]
                else:
                    i += 1
        return result
                





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans) == 0:
            print("[]", end="")
        for value in ans:
            print(value, end=' ')
        print()

# } Driver Code Ends