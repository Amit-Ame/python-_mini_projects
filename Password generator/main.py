import string
import random 

s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.digits
s4=string.punctuation

plen = int(input("enter length:"))
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

random.shuffle(s)
print("".join(s[0:plen]))