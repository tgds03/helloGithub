#!/usr/bin/python3
import sys
import re

file = open(sys.argv[1], 'r')
n = int(sys.argv[2])

# tokens = "".join( [chr(i) for i in range(128) if not chr(i) in string.ascii_letters + string.digits] )
text = file.read()
pattern = re.compile('\w+')
wordlist = re.findall(pattern, text)

freq = {}
for word in wordlist:
	if word.lower() in freq:
		freq[word.lower()] += 1
	else:
		freq[word.lower()] = 1

result = sorted(freq.items(), key=lambda x: x[1], reverse=True)


for i in range(n):
	print(f"{result[i][0]} : {result[i][1]}")