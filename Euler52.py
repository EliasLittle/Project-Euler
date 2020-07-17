def test(n):
	list = [set(str(2*n)),set(str(3*n)),set(str(4*n)),set(str(5*n)),set(str(6*n))]
	if all([l == set(str(n)) for l in list]):
		return True
	return False
	
for i in range(123456,9999999):
	if test(i):
		print("Answer:"+str(i))
		break
