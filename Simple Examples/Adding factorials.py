# Given an integer n, print the sum 1!+2!+3!+...+n!.
# This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

sum=0
for i in range(1,int(input())+1):
    sum+=i