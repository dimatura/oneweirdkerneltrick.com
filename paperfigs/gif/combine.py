#!/usr/bin/python

import random, os

seq = [None]
while len(seq) != 10:
    s = random.randint(1,6)
    if seq[-1] != s:
        seq.append(s)
seq = seq[1:]

com = "convert "
for s in seq:
    com += "ad%d.jpg " % s

com += " -resize 500 -set delay 50 -verbose output.gif"

os.system(com)




