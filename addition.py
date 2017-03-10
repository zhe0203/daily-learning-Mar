A_1 = input(r'输入数据:')
B_1 = input(r'输入数据:')

if len(A_1) >= len(B_1):
    A = A_1
    B = B_1
else:
    A = B_1
    B = A_1

a = []
b = 0

for i in range(len(B)-1,-1,-1):
    num = int(A[i+(len(A)-len(B))]) + int(B[i]) + int(b)
    if num >= 10:
        a.append(str(num)[-1])
        b = str(num)[0]
    else:
        a.append(str(num))
        b = 0

if int(b) >= 1:
    a.append(str(int(A[len(A)-len(B)-1]) + int(b)))
else:
    a.append(str(int(A[len(A)-len(B)-1])))

last = A[0:(len(A) - len(B)-1)]

a.append(last)
a.reverse()
print(r'竖式计算结果:',''.join(a))
print(r'内置运算结果:',int(A)+int(B))
