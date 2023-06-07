#!/usr/bin/python3

def uppercase(str):
    for ii in str:
        if ord(ii) >= 97 and ord(ii) <= 122:
            cc = chr(ord(ii) - 32)
        else:
            cc = ii
        print("{}".format(cc), end="")
    print()
