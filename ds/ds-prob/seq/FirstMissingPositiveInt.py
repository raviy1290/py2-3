class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        l = len(A)
        for i in range(l) :
            elem = A[i]
            pos = elem - 1

            if pos >= 0 and pos < l and A[pos] != elem:
                A[i], A[pos] = A[pos], A[i]
        
        print(A)

s = Solution()
print(s.firstMissingPositive([-1, 2, 3, 0]))
