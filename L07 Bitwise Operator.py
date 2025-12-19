#Left shifts
a=14
b=6

print("a << 1=", a<<1,"\n"+ "b << 1=", b<<1, "\n")

#Right Shifts
a=18
b=-9

print("a >> 1=", a>>1,"\n"+ "b >> 1=", b>>1, "\n")

#And
a=2
b=4
c=2
d=8
if (a is b)&(a is c):
    print("a has the same value as b and c.")

#Or
if (a is b)|(a is c):
    print("a is either equal to b or c.")

#XOR
if (a is b)^(a is c):
    print(True)

if (a is b)^(a is d):
    print(False)