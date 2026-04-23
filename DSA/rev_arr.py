class Solution:
    def reverse(self, i, arrs):
        n = len(arrs)
        if i >= n//2:
            return
        else:
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
            self.reverse( i+1, arr)
        
          
arr = [2,4,6,8]

# reverser = Solution.reverse( 0, arr)   --> wrong way of doing it, first make an instance

sol = Solution()
sol.reverse(0, arr)
print(arr)
