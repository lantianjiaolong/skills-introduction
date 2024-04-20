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

# 第2种：
BMI = 22
if BMI <= 18.6:
    print('偏瘦')
else:
    if BMI <= 25:
        print('正常')
    else:
        if BMI <= 28:
            print('超重')
        else:
            if BMI <= 32:
                print('肥胖')
            else:
                print('非常肥胖')