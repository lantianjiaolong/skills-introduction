"""
初聊for循环:
          1.如果某一个数据,可以循环调用?
          2.如果某一项操作,需要重复处理?

          你需要循环了~
"""

# 1.如果某一个数据中的元素,需要被逐个循环调用?
# a = 'abcdefg'
#
# for i in a:
#     print(i)
#     print('我爱你')


# 2.如果某一项操作,需要重复执行指定次数?   左闭右开区间  包头不含尾
# for i in range(0, 10000):    # range()函数:第1个参数填起始数字,第2个参数填结束数字(不包含)
#     # print(i)
#     print('Python是世界上最好的语言')


# for i in range(10000):  # 默认从0开始, 0-9999
#     # print(i)
#     print('Python是世界上最好的语言', end='\n')

# print('哈哈哈哈哈哈')


# 利用for循环和range函数实现连续整数的累加:1-100
# sum = 0
#
# for i in range(1, 101):
#     sum += i  # sum = sum + i
#
# print("总和:", sum)


# 利用for循环和range函数实现连续整数的累乘
# product = 1
#
# for i in range(1, 101):
#     product *= i  # product = product * i
#
# print("累乘结果:", product)


# 利用for循环,反转字符串
# a = "I love Python"
# a = 'abc'  # 'cba'
# b = ''
#
# for i in a:
#     b = i + b  # a ba cba
#     # print(b)
#
# print("反转后的字符串:", b)


# 利用for循环,过滤字符串中的空格符号
# a = "Hello World 哈哈哈哈哈哈"
# b = ""
#
# for i in a:
#     if i != ' ':
#         b += i  # b = b + i
#
# print("过滤后的字符串:", b)


"""
通常可以被for循环 迭代 (迭代是一种遍历集合(非Python的集合数据类型)元素的方式)的数据,
我们也称之为:或者可迭代对象(Python中,一切皆对象)
"""


"""
变量交换
"""
# a = 1
# b = 2
# 要求a,b值互换,怎么实现?

# a = b  # a = b = 2  >>  a = 2
# b = a  # b = a = 2  >>  b = 2
#
# print(a)
# print(b)


# 常规方法(引入1个第3方变量)
# a = 1
# b = 2
#
# c = a   # c = 1
# a = b   # a = 2
# b = c   # b = 1
# print(a)
# print(b)


# Python方法
# a = 1
# b = 2
#
# a, b = b, a
# print(a)
# print(b)


"""
异常捕获
"""
# 是否会报错?
# a = 1
# b = '4'
# print(a + b)
# print('hello world')

# try ... except 语句捕获异常,代码不会因为报错而停止运行

# a = 1
# b = '2'
# try:  # 尝试运行
#     print(a + b)     # 1
#     print('运算完成')  # 2
#
# except Exception as e:  # 不然
#     print('hello world')  # 3
#     print(e)   # 4


# try...except...else...finally
# a = 6
# b = 5
# try:  # 实验代码                          一
#     print(a + b)        # 1
#     print('运算完成')    # 2
#
# except Exception as e:  # 出现异常后执行   二
#     print(e)            # 3
#     print('已出现异常')   # 4
#
# else:  # 未出现异常执行                   三
#     print('没有出现异常')  # 5
#
# finally:  # 最终都会执行                   四
#     print('运行完毕')     # 6

# print('运行完毕')    # 7


# 捕获类型转换错误
# a = input('请输入1个数字:')
# try:
#     a = int(a)
#     print(a)   # 1
# except Exception as e:  # 取别名
#     print(e)   # 2
#     print('该元素不能转换为整数类型')  # 3
# else:
#     b = a + 1
#     print(b)   # 4
# finally:
#     print('运行结束')  # 5


# for循环 + 异常捕获语句获取字符串中数字的倒数

# strs = 'abc123def456'
#
# for i in strs:
#     try:
#         i = int(i)
#         result = 1 / i
#     except Exception as e:
#         print("不能得到倒数")
#         print(i)
#     else:
#         print("倒数:", result)
#     finally:
#         print('计算结束')
