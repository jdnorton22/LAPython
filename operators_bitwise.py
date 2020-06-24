# AND OR XOR 
# & | ^ 
a=0b1001
b=0b1100

>>> a=0b1001
>>> b=0b1100
>>> a|b
13  
>>> bin(a|b)
'0b1101'
>>> bin(a&b)
'0b1000'
>>> bin(a^b)
'0b101'

a=0b110
bin(a>>2) #shifts 2 digits right
0b1 (1)
bin(a<<2) #shifts to digits left
0b11000 (24)