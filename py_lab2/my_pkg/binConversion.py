def binConversion(s):
	# n = 0
	# for i in range(len(s)):
	# 	if s[i] == '1':
	# 		n += 2**(len(s)-i-1)
	n = int(s, 2)
	
	return (oct(n)[2:], str(n), hex(n)[2:])

if __name__=="__main__":
	s = input()
	print(binConversion(s))
