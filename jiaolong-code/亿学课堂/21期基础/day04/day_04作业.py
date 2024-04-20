# 请把下面代码改写为只用if 和 else (数量不定)的判断语句(不准用elif)

w = int(input('请输入您的体重:(单位:kg)'))
H = int(input('请输入您的身高:(单位:cm)'))
BMI = w / ((H/100) ** 2)
if BMI < 18.5:
    print('偏轻')
if 18.5 <= BMI and BMI <= 25:
    print('正常')
if 25 < BMI and BMI <= 28:
    print('超重')
if 28 < BMI and BMI <= 32:
    print('肥胖')
if BMI > 32:
    print('非常肥胖')