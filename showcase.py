#!/usr/bin/env python3

import getch

print("Would you like to continue? y/n")
check = getch.getch()
if check == 'y':
	print("Yay!")
elif check == 'n':
	print(":(")
else:
	print("Please state y or n")