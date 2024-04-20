# 1.运用for循环和if判断,把0-100里所有的偶数打印出来

# 方法1
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')

print()
# 方法2 
for i in range(0, 101, 2):  # 步长
    print(i, end=' ')

print()
# 2.运用for循环和if判断,把0-100里所有被3除余1的数字打印出来

for i in range(0, 101):
    if i % 3 == 1:
        print(i, end=' ')


