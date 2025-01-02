#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
        pc={0:1}
        s=0
        c=0
        for i in arr:
            s+=i
            if s-k in pc:
                c+=pc[s-k]
            pc[s]=pc.get(s,0)+1
        return c
        # s=0
        # csum=0
        # c=0
        # for i in range(len(arr)):
        #     csum+=arr[i]
        #     while csum>k and s<=i:
        #         csum-=arr[s]
        #         s+=1
        #     if csum==k:
        #         c+=1
        # return c
        # l=[]
        # c=0
        # for i in range(len(arr)):
        #     for j in range(i,len(arr)):
        #         a=arr[i:j+1]
        #         l.append(a)
        # # print(l)
        # for i in l:
        #     if sum(i)==k:
        #         c+=1
        # return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends