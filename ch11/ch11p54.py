#!/bin/python
s1 = str(input())
s2 = str(input())
s3 = str(input())
s4 = str(input())
s1 = s1[0:s1.find(s2)] + s1[s1.find(s2)+len(s2):]
s1 = s1[0:s1.find(s3)+len(s3)] + s4 + s1[s1.find(s3)+len(s3):]
print(s1)
