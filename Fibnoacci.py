cached ={}
def fibnoacci(n):
	if n in cached:
		return cached[n]
	elif n == 1 or n== 2:
		return 1
	else:
		value = fibnoacci(n-1) + fibnoacci(n-2)
		cached[n] = value
		return value
print(fibnoacci(int(input())))
