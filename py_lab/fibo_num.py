#!/usr/bin/python3
print("fibonacci number?", end=' ')
n = int(input())

arr = [1, 1]
for i in range(3, n+1):
	arr.append(arr[len(arr)-1]+arr[len(arr)-2])

print(arr)
print( "F%d = %d" % (n, arr[len(arr)-1]) )
