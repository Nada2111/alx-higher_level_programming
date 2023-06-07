#!/usr/bin/python3
for ii in range(0, 10):
    for jj in range(1, 10):
        if ii >= jj:
            continue
        elif ii == 8 and jj == 9:
            print("{}{}".format(ii, jj))
        else:
            print("{}{}, ".format(ii, jj), end="")
