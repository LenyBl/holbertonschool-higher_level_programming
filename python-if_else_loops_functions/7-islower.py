#!/usr/bin/python3
def islower(c):
	"""Check if a character is lowercase.

	Args:
		c (str): A single character string.
	Returns:
		bool: True if c is lowercase, False otherwise.
	"""
	if 'a' <= c <= 'z':
		return True
	elif c == "":
		return False
	else:
		return False
