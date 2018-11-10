def factt(n) :
	fact = 1
	if n <= 1 :
		return fact
	for i in range(2, n+1) :
		fact *= i
	return fact
    
def convertList(n) :
    l = []
    while n > 10 :
        l.append(n % 10)
        n = n//10
        
    l.append(n)
    return l
    

f = factt(9)
print(f)
ll = convertList(f)
print(ll[-1], len(ll)-1)