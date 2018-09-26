import pprint

def lcs(X , Y): 
    # find the length of the strings 
    m = len(X) 
    n = len(Y) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(n+1) for i in range(m+1)] 
    pprint.pprint(L) 
    """L[i][j] contains length of LCS 
    of 
    i elem of x X[0..i-1] 
    and 
    j elem of Y[0..j-1]"""
    
    for i in range(m+1): 
        for j in range(n+1): 
        	#if any seq is of 0 lenth the lcs = 0
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    pprint.pprint(L)
    return L[m][n] 
#end of function lcs 

X = "AGGTAB"
Y = "AGXTXAYB"

print(lcs(X, Y))