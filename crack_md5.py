#!/usr/bin/python


import hashlib
import os
import time
import sys

TGREEN =  '\033[32m'
print(TGREEN + '          _____                            _____          ')
print(TGREEN + '         /\    \                          /\    \         ')
print(TGREEN + '        /::\    \                        /::\____\        ')
print(TGREEN + '       /::::\    \                      /:::/    /        ')
print(TGREEN + '      /::::::\    \                    /:::/    /         ')
print(TGREEN + '     /:::/\:::\    \                  /:::/    /          ')
print(TGREEN + '    /:::/  \:::\    \                /:::/____/           ')
print(TGREEN + '   /:::/    \:::\    \              /::::\    \           ')
print(TGREEN + '  /:::/    / \:::\    \            /::::::\    \   _____  ')
print(TGREEN + ' /:::/    /   \:::\    \          /:::/\:::\    \ /\    \ ')
print(TGREEN + '/:::/____/     \:::\____\        /:::/  \:::\    /::\____\ ')
print(TGREEN + '\:::\    \      \::/    /        \::/    \:::\  /:::/    /')
print(TGREEN + ' \:::\    \      \/____/          \/____/ \:::\/:::/    / ')
print(TGREEN + '  \:::\    \                               \::::::/    /  ')
print(TGREEN + '   \:::\    \                               \::::/    /   ')
print(TGREEN + '    \:::\    \                              /:::/    /    ')
print(TGREEN + '     \:::\    \                            /:::/    /     ')
print(TGREEN + '      \:::\    \                          /:::/    /      ')
print(TGREEN + '       \:::\____\                        /:::/    /       ')
print(TGREEN + '        \::/    /                        \::/    /        ')
print(TGREEN + '         \/____/                          \/____/         ')
print('                                                                   ')
time.sleep(3)


def tryOpen(wordlist):
	global pass_file
	try:
		pass_file = open(wordlist, "r")
	except:
		print("[!!]No Such File at That path!")
		quit()

pass_hash = sys.argv[1]
wordlist = sys.argv[2]
tryOpen(wordlist)

def crack():
	for word in pass_file:
		print("[-]trying: " + word.strip("\n"))
		enc_wrd = word.encode('utf-8')
		md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()
		os.system("clear")
		if md5digest == pass_hash:
			print("[+]Password Found: " + word)
			exit(0)
crack()
print("[!] Password Not In list")
