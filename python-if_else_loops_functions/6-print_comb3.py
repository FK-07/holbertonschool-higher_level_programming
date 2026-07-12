#!/usr/bin/python3
for i in range(1, 90):
    if i == i*10:
        continue
    print("{:02d}".format(i))
