# 请把下面代码改写为只用多个if 和 else 的判断语句(不准用elif)
# W = int(input('请输入你的体重:(单位:kg)'))
# H = int(input('请输入你的身高:(单位:cm)'))
# BMI = W / ((H/100) ** 2)
# BMI = 22
# if BMI < 18.6:
#     print('偏瘦')
# elif BMI <= 25:
#     print('正常')
# elif BMI <= 28:
#     print('超重')
# elif BMI <= 32:
#     print('肥胖')
# else:
#     print('非常肥胖')
# print('计算结束')


# 第3种：
BMI = 22
if BMI <= 18.6:   # 1
    print('偏瘦')
if 18.6 < BMI <= 25:   # 2
    print('正常')
if 25 < BMI <= 28:   # 3
    print('偏重')
if 28 < BMI <= 32:   # 4
    print('肥胖')
if BMI > 32:
    print('非常肥胖')
# else:  # 换成else呢？ 结果是非常肥胖和前面的正常相矛盾！
#     print('非常肥胖')