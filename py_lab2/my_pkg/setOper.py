
def setOper(s1, s2):
	set1 = set(map(int, s1.replace('[', '').replace(']', '').split(',')))
	set2 = set(map(int, s2.replace('[', '').replace(']', '').split(',')))
	union = set1.union(set2)
	inter = set1.intersection(set2)
	return union, inter


if __name__=='__main__':
	print(setOper('[1, 2, 3, 4]', '[1, 2, 5, 6]'))