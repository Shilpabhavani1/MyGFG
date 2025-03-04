class Solution:
    def lis(self, arr):
        # code here
        sub = []
        for i in arr:
            l, r = 0, len(sub)
            while l < r:
                m = (l + r) // 2
                if sub[m] < i:
                    l = m + 1
                else:
                    r = m
            if l == len(sub):
                sub.append(i)
            else:
                sub[l] = i
        return len(sub)
       



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends