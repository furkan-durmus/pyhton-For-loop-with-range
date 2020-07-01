# For the given integer N calculate the following sum:
# 1<3>+2<3>+…+N<3>
t=0
for i in range(1,int(input())+1):
    t+=i**3
print(t)