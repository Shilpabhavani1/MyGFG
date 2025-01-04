
class Solution:
    def countTriplets(self, arr, target):
        n = len(arr)
        count = 0
    
    # Iterate through the array
        for i in range(n - 2):
            left, right = i + 1, n - 1
        
        # Two-pointer approach for the remaining array
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
            
                if current_sum == target:
                # Handle duplicates for left and right values
                    if arr[left] == arr[right]:
                    # All pairs between left and right are valid
                        count += (right - left + 1) * (right - left) // 2
                        break
                
                # Count all valid combinations for the current left and right
                    l_count = 1
                    r_count = 1
                
                # Move left pointer and count duplicates
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        l_count += 1
                        left += 1
                
                # Move right pointer and count duplicates
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        r_count += 1
                        right -= 1
                
                # Add the product of counts of duplicates
                    count += l_count * r_count
                
                # Move pointers to continue
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # Increase sum by moving left pointer
                else:
                    right -= 1  # Decrease sum by moving right pointer
                
        return count

    # def countTriplets(self, arr, target):
    #     # code here
    #     n=len(arr)
    #     c=0
    #     for i in range(n):
    #         left=i+1
    #         right=n-1
    #         while left < right:
    #             csum=arr[i]+arr[left]+arr[right]
    #             if csum==target:
    #                 c+=1
    #                 left+=1
    #                 right-=1
    #             elif csum<target:
    #                 left+=1
    #             else:
    #                 right-=1
    #     return c


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends