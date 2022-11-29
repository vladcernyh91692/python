def chislo(n):
	if n==0:
		return 0
	return n%10+chislo(n//10)
print(chislo(2850))
