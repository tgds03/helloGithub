#!/usr/bin/python
print("fibonacci number?", end=' ')
n = int(input())

arr = [1, 1]
for i in range(3, n+1):
	arr.append(arr[len(arr)-1]+arr[len(arr)-2])

print(arr)
print(arr[len(arr)-1])