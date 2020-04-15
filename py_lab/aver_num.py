#!/usr/bin/python
print("Enter number of input : ", end='')
n = int(input())
sum = 0

for i in range(n):
	sum += int(input())

avg = sum/n
print(avg)