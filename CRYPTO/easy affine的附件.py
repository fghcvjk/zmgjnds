# -*- coding: utf-8 -*-
import string
import hashlib
from Flag import m,a,b

letter=string.ascii_letters+string.digits

def encrypt(m, c, a, b):
    for i in range(len(m)):
        ch=m[i]
        t=(letter.index(ch) * a + b) % 62
        c.append(letter[t])
    d = ''.join(c)
    print (d)

m = ????
c = []
a = ????
b = ????

assert ("Flag" in m)

print("加密后的密文为：")
Cipher = encrypt(m, c, a, b)
flag = hashlib.md5("".join(str(m))).hexdigest()

"""
加密后的密文为：
YWINN4R2bEmp4blzqpm2waT2KRCayj7C5TCp2wpvl0y
"""
