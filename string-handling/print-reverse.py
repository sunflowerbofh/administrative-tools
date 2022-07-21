#!/usr/bin/python
# Print string the other way round (like 'tac' for files),
# e.g. python print-reverse.py 3.1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.5.0.2.1.1.0.c.9.f.4.0.1.0.a.2
# -> 2.a.0.1.0.4.f.9.c.0.1.1.2.0.5.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.1.3

import sys

def reverse(x):
	return x[::-1]

text = reverse(sys.argv[1])
print(text)
