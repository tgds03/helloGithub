#!/usr/bin/python3
import my_pkg as pkg

if __name__=='__main__':
	while(1):
		print("Select Menu: 1) conversion 2) union/intersection 3) exit >> ", end='')
		n = input()
		if n == '1':
			print("input binary number : ", end='')
			try:
				a = pkg.binConversion(input())
				print("OCT> {}\nDEC> {}\nHEX> {}".format(a[0], a[1], a[2].upper()))
			except ValueError:
				print("invaild input")

		elif n == '2':
			print("Typing 1st list : ", end='')
			str1 = input()
			print("Typing 2st list : ", end='')
			str2 = input()
			a = pkg.setOper(str1, str2)
			print( "union {}\nintersection {}".format(list(a[0]), list(a[1])) )

		elif n == '3':
			print("exit the program")
			break
		else:
			print("invaild menu")

