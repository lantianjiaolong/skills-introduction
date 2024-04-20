"""
条件判断
"""
# a = 1
# b = 2
# 如果:
# if a < b:  # bool
#     print('Python是世界上最好的语言')  # 1
#     print('Python是世界上最好的语言')
# else:      # 其他的
#     print('好的')  # 2
#
# print('哈哈哈哈')  # 3


# a = input('请输入数字:')  # '16'
# b = 16
# c = int(a)
# if c == b:
#     print('a等于b')
# else:
#     print('a不等于b')


# 层层递进(缩进)
# a = 5
# if a > 0:
#     print('你通过了第1关')  # 1
#     if a > 6:
#         print('你通过了第2关')  # 2
#         if a > 4:
#             print('你通过了第3关')  # 3


# a = 5
# if a > 0:
#     print('你通过了第1关')  # 1
#
# if a > 6:
#     print('你通过了第2关')  # 2
#
# if a > 4:
#     print('你通过了第3关')  # 3


# a = 9
# if a < 0:
#     print('哈哈哈哈')  # 1
#
# else:  # a >= 0
#     if a > 10:
#         print('a大于10')  # 2
#     else:
#         print('a大于等于0并且a小于等于10')  # 3


# 插讲2个运算符 %:取余, //:取整
# a = 10 % 2  # 一个数能不能被另一个数整除 : 余数为0
# print(a)
#
# a = 10 % 3
# print(a)
#
# b = 10 // 2
# print(b)
#
# b = 10 // 3
# print(b)


# 看PPT
# 计算一个年份是否是闰年: (四年一闰，百年不闰，四百年再闰)
# year = int(input('请输入一个年份:'))
#
# if year % 4 == 0:  # 1
#     if year % 100 == 0:  # 2
#         if year % 400 == 0:
#             print('此年份是闰年')   # 3
#         else:  # year % 400 != 0
#             print('此年份不是闰年')  # 3
#     else:  # year % 100 != 0 # 2
#         print('此年份是闰年')     # 能够被4整除，并且不能被100整除
# else:  # year % 4 != 0   # 1
#     print('此年份不是闰年')


# if 和 elif的区别:
# a = 15
#
# if a > 16:
#     print('哈哈')  # 1
#
# elif a > 12:   # 改elif
#     print('呵呵')  # 2
#
# elif a > 9:   # 改elif
#     print('呵呵')  # 3
#
# else:
#     print('嘿嘿')  # 4


# 表示体重kg，l表示身高cm
# BMI = 体重（kg）÷ 身高^2（m）
# 例如: 体重 = 70kg , 身高 = 175cm = 1.75m
#      BMI = 70kg ÷（1.75×1.75）= 22.86
"""
BMI(体质指数) = 体重(kg) ÷ 身高(m)^2
   BMI值            状态
      BMI<18.5      偏瘦
18.5<=BMI<=25       正常
   25<BMI<=28       超重
   28<BMI<=32       肥胖
   32<BMI         非常肥胖
"""
# w = int(input('请输入您的体重:(单位:kg)'))
# H = int(input('请输入您的身高:(单位:cm)'))
# BMI = w / ((H/100) ** 2)

# BMI = 16
# 如果用if语句:
# if BMI < 18.5:
#     print('偏轻')  # 1
# if BMI <= 25:
#     print('正常')  # 2
# if BMI <= 28:
#     print('超重')  # 3
#
#
# if BMI <= 32:
#     print('肥胖')  # 4
# else:
#     print('非常肥胖')  # 5


# BMI = 24
# # 如果用if和elif:
# if BMI < 18.5:     # 范围:由小到大
#     print('偏轻')   # 1
#
# elif BMI <= 25:
#     print('正常')   # 2
#
# elif BMI <= 28:
#     print('超重')   # 3
#
# elif BMI <= 32:
#     print('肥胖')   # 4
#
# else:
#     print('非常肥胖')  # 5


# 如果换成范围从大到小
# BMI = 24
# if BMI < 32:
#     print('肥胖')  # 1
# elif BMI <= 28:
#     print('超重')  # 2
# elif BMI <= 25:
#     print('正常')  # 3
# elif BMI <= 18.5:
#     print('偏瘦')  # 4
# else:
#     print('非常肥胖')  # 5


"""
运算与优先级
"""
# 四则基本运算
# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# 取整与取余
# print(a // b)
# print(a % b)


# divmod()函数 :一次运算 取整 加 取余
# 10除以3
# a = divmod(10, 3)
# print(a)  # 结果:(x,y) 元组  x:取整 y:取余
# 5除以2
# b = divmod(5, 2)
# print(b)


# 幂函数(次方)
# a = 2
# b = 3
# 表达式
# c = a ** b
# print(c)


# pow函数
# a = 2
# b = 3
# c = pow(a, b)  # a:底数 b:次方数
# print(c)


"""
优先级
"""
# 先乘除(包含取整取余)再加减
# print(1+2*3)
# print(1+2/3)
# print(1+2//3)
# print(1+2 % 3)

# 也可以通过小括号改变运算顺序
# print( (1+2)*3 )

# 多层小括号运算
# a = 1
# b = 2
# c = a * (a + b % a) + (a - b*(b + b))
# print(c)


# and(和) 与 or(或)

# and:and 两边均满足要求
# a = 6
# if (a % 2 == 0) and (a % 3 == 0):
#     print('该数能被2和3整除')
# else:
#     print('该数不符合要求')

# or: or 至少有一边满足要求
# a = 6
# if (a % 3 == 0) or (a % 2 == 0):
#     print('该数能被2或3整除')
# else:
#     print('该数不符合要求')


# 练习题  定性原则
# 1.确定整个式子的bool值;
# 2.输出决定式子bool值的元素.

# print(True or True)
# print(False or True)
# print(False and True)
# print(True and True)
# print(True and False)

# print(1 or 2)   # True  1
# print(0 or 1)   # True  1
# print(0 and 10000)  # False 0
# print(1 and 0)    # False
# print(1 and 2)  # True  2

# 拓展题
a = 1 or 2 and 3 or 4 and 5 or 6
# 1 or (2 and 3) or (4 and 5) or 6
#  1 or 3 or 5 or 6
#    1 or 5 or 6
#      1  or  6
#          1

# print(a)


# 结合判断逻辑，我们可以定义一个判断年份是否是闰年的代码
# year = int(input('请输入需要判断的年份:'))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('该年份是闰年')
# else:
#     print('该年份不是闰年')
































