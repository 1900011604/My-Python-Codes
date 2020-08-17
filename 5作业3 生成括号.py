n = 2 * int(input())
result = []
for i in range(2 ** n):
	str1 = bin(i)[2:]
	str1 = '0' * (n - len(str1)) + str1
	if str1.count('1') == str1.count('0'):
		str1 = str1.replace('0','(').replace('1',')')
		str2 = str1.replace('(','(0,').replace(')','),')
		try:
			a = eval(str2)
		except:
			pass
		else:
			result.append(str1)
for str3 in result:
	print(str3)
