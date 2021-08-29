from Crypto.Util.number import *
import binascii
import gmpy2
flag = '*****************************************'
hex_flag=int(flag.encode("hex"),16)

p=getPrime(256)
q=getPrime(256)
n=p*q

e=0x3
c1=pow(hex_flag,e,n)
c2=pow(hex_flag+1,e,n)


print("n=",hex(n))
print("e=",hex(e))
print("c1=",hex(c1))
print("c2=",hex(c2))

'''
('n=', '0xb28ae8f29f8b90e8b8c5667b2b71e49929446b41f7f7a3e9e45bc52a1e8c45d59c1788be48a9c365d51feee0b2cd3295001cdad1ba5ccf808686b5ce5a269ae5L')
('e=', '0x3')
('c1=', '0x7ba5502ecbc3b15ad8c2db8f30a593eb062dde4d7dfacadf0a28291d1a576389a18dfba0607c0243f843f637449089dd2090d47ee9845d4147f02afd4d891f19L')
('c2=', '0x891ac4f663df41c1f6433ee3513d749c3ba02fe0aacd7f51d791b9bac4f7e5194bd484d78d972c344faf600f7d3aa580485774768efc47ab8ddb67eeeb330fa1L')

'''