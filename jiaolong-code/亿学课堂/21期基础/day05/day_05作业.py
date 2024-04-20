# 1.运用for循环和if判断,把0-100里所有的偶数打印出来

# 2.运用for循环和if判断,把0-100里所有被3除余1的数字打印出来

for i in range(0, 101):
    if i % 2 == 0:    # 判断是否是2的倍数
        print(i)
    

for i in range(0, 101):
    if i % 3 == 1:    # 判断是否被3除余数是1
        print(i)


        