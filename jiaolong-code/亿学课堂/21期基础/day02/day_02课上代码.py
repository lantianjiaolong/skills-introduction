"""
字面量:被写在代码中的固定的值
例如:数字,文字
"""
# 666
# '我爱你'
#
# print(666)
# print('我爱你')


"""
变量:  在程序中,用来存储计算结果或者表示某个值的抽象的一个概念
      好比,给某个值取一个名字(标识符),通过这个名字(标识符),我们就能找到这个值

      变量的定义格式: 变量名称 = 变量的值
                        a  = 666
见PPT
"""

# a = 666
# a = '我爱你'
# a = 888
# print(a)

# A = 999
# print(A)
# print(a)

# b = '我爱你'
# print(b)


"""
数字与字符串
"""

# 数字:数字分为 整数 和 浮点数(小数)
# 整数
# a = 1
# print(a)  # 打印函数
# type(a)  # 类型函数
# print(type(a))  # int 整数类型
#
# b = 100
# print(b)
# print(type(b))


# print(a+b)
# print(type(a+b))

# a + b = c

# c = a + b
# print(c)
# print(type(c))


# 浮点数
# a = 1.5
# print(a)
# print(type(a))
# b = 101.25
# print(b)
# print(type(b))
#
# c = a + b
# print(c)
# print(type(c))

# a = 1.5
# b = 1.5
# c = a + b
# print(c)
# print(type(c))


# d = 3.0
# print(d)
# print(type(d))

# 整数可以和浮点数相加或相乘吗?
# a = 1.5
# b = 2
# c = a + b
# d = a * b
# print(c)
# print(type(c))
# print(d)
# print(type(d))

# a = 3
# b = 3
# c = a / b
# print(c)
# print(type(c))


# 求绝对值

# a = -2.0
# c = abs(a)
# print(c)
# print(a)


# 字符串
# a = '我爱你'
# 由0个或者多个字符组成的有限序列.
# 通常用来表示文本类的数据,例如:在代码里显示:我爱你~
# 字符串数据通常由引号包围起来 (英文标点:单引号,双引号都可以,但是要成双成对)
# 例如: '我爱你' , '哈哈哈哈'


# a = ''  # 空字符串
# a = '我爱你'
# print(a)
# print(type(a))
# b = "哈哈哈哈"
# print(b)
# print(type(b))


# c = a + b
# print(c)
# print(type(c))
# d = b + a
# print(d)
# print(type(d))


# a = '我爱你'
# b = 10
# c = a * b
# print(c)
# print(type(c))


# 也可以用3对引号表示:
# 作用是可以保留字符串格式
# 1对引号的字符串不能保留原有格式
# a = "abcd
#  a
#
#  bbb"


# 看下3对引号的字符串
# b = '''abcd
# a
#
# bbb'''
#
#
# b = """abcd
# a
#
# bbb"""
#
# print(b)


# 字符串单双引号混合使用的作用
# 成双成对,就近匹配
# a = "那女孩对我说:'你是一个小偷'"
# print(a)


# a = 1
# print(a)
# print(type(a))
#
# b = '1'
# print(b)
# print(type(b))

"""
输入与输出:
"""
# 输出: print() 函数(内置函数)
# print('Hello World')
# print(1)


# 输入: input()函数
# a = input()
# print(a)


# input函数参数
# a = input('请输入你想说的话:')  # 提示语句
# print(a)


"""input()函数特点:"""
# input函数输入数据特点:
# a = input('请输入一个数字:')  # 键盘输入: 100  代码里: '100'
# print(a)
# print(type(a))  # type()   123 -- '123'

# a = 123  # 整数 int
# print(a)
# print(type(a))
# b = '123'  # 字符串 str
# print(b)
# print(type(b))

# a = input('请输入你的年龄:')  # 字符串（文字)   数字:18
# print(a)  # '18'
# print(type(a))  # type(a)

# a = 1
# b = input('请输入数字:')  # 1   '1'
# print(a+b)


"""数据类型转换"""
# a = 123
# print(type(a))  # int
# b = '123'
# print(type(b))  # str

# c = int(b)  # str >> int
# print(c)
# print(type(c))
#
# print(b)  # str
# print(type(b))


# d = '我爱你'   # '520'?
# e = int(d)
# print(e)


"""万物皆可字符串"""
# a = 2
# b = str(a)
# print(b)
# print(type(b))
#
# a = 1.25
# b = str(a)
# print(b)
# print(type(b))

# a = '1.25'
# b = float(a)
# print(b)
# print(type(b))


"""
如果把浮点数转化为整数呢 
"""
# a = 2.75
# b = int(a)
# print(b)


# b = input('请输入一个数字:')
# print(b)
# print(type(b))
# c = int(b)  # int():只针对符合要求的字符串有效   '123'
# print(c)
# print(type(c))
#
# a = '1.5'
# b = float(a)  # '10'
# print(b)
# print(type(b))
#
# a = 2
# b = float(a)
# print(b)
# print(type(b))


# 注释: 提醒,解释,说明 (不参与代码的实际运行)
# 打印 hello world这句话
# print('hello world')  # 打印 hello world这句话
# 打印 hello world这句话

# print('你好我好大家好')


# 第1种方式(单行注释): 代码前加: # (快捷方式:选中要注释的代码,按住 ctrl键,再按 ? 问号键)
# a = 1  # 这是一个数字1   快捷键 : ctrl + ?


# 第2种方式(多行注释):  """注释解释说明"""  (前面不加变量名接收)
"""
哈哈
哈哈
哈哈
这是注释说明
"""


"""变量赋值"""
# a = 1  # 意思是:把1赋值给a
# a = 2
# print(a)
# a = 1
# print(a)
# a = 2
# print(a)


# a = 1
# A = 2
# print(a)
# print(A)


# a = 1
# print(a)

# a = a + 1
# a += 1
# print(a)


# id() 函数:数据内存地址,也可以看做是一个唯一标识符,每个数据都不一样
# a = 1
# print(a)
# print(id(a))
#
# b = 2
# print(b)
# print(id(b))


# a = 1
# b = a
# print(id(a))
# print(id(b))


