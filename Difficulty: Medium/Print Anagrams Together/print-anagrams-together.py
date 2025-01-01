#User function Template for python3


class Solution:

    def anagrams(self, arr):
        l=[]
        for i in arr:
            m=[]
            # m.append(i)
            for j in arr:
                if sorted(i)==sorted(j):
                    m.append(j)
            if m not in l:
                l.append(m)
        # print(l)
        return l
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends