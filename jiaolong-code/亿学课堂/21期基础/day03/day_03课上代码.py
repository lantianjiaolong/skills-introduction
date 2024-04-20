"""
字符串的加法和乘法:
"""
# 加法
# a = 'I love'
# b = 'Python'
# print(a+b)
# print(b+a)


# 乘法
# a = 'Python是世界上最好的语言~'
# print(a * 10)

# print('\n')
# a = 'Python is the best program language\n'  # 这里的\n表示换行
# print(a * 10)


"""
转义字符:字符在Python 字符串 里已经有了特殊意义，
但在字符串里可能需要它们显示原有的样子,所以进行转义
"""
# 例如:
# print('123')
# print('\n')

# 也许你的字符串是一个文件的路径
# print('D:\Python\theOne\two\new\basic')

# 这里打印的字符串并不是你想要的文件路径
print('哈哈哈哈哈哈\r呵呵')
print('哈哈哈哈哈哈\n呵呵')


# print('那女孩对我说:'你是个好人'')
# print("那女孩对我说:'你是个好人'")  # 不使用转义字符

# print('那女孩对我说:\'你是个好人\'')  # 使用转义字符
# 转义字符串(先下手为强)
# print('\\')
# print('D:\\Python\\theOne\\two\\new\\basic')


# 如果觉得使用转义字符太繁琐了，所以我们可以用原始字符串
# 原始字符串
# print(r'D:\Python\theOne\two\new\basic')  # raw


# 布尔类型数据  True False
# ==  判断左右是否相等
a = True
b = False
# print(type(a))
# print(type(b))


# a = 1
# b = 2
# print(a == b)  # True /  False  bool数据类型
# print(a != b)   # 判断左右2边是否不相等


# 任何数据都是有bool属性  bool()
# print(bool(0))
#
# a = bool(1.5)  # 数字:非0即为真
# print(a)

# a = bool('')  # 字符串:非空即为真
# print(a)

"""
身是菩提树，心如明镜台，时时勤拂拭，勿使惹尘埃    0  or ''

菩提本无树，明镜亦非台，本来无一物，何处惹尘埃     None
"""

# None类型(空值)：None
# a =
b = None

# print(bool(None))
# print('' == None)
# print(0 == None)
# print(0 == '')


# 编码格式
"""
在计算机中，每个字符都由一个或多个二进制数字表示
例如:字母"A"对应的二进制代码是01000001。
当我们在文本文件中输入字母"A"时，
计算机会根据ASCII编码将其转换为二进制代码01000001，然后存储和处理该二进制数据
ASCII编码一共包含128个字符与二进制代码的对应关系
"""

# 位 (bit)  二进制中的 0 和 1 都叫 1 个位
# 字节(Byte) 8个位 二进制位 组成 1个字节
# 2*2*2*2*2*2*2*2 = 256

#  Unicode -- utf-8

"""
比较运算符
"""
# 1.比较判断:
# <:小于
# a = 1
# b = 2
# print(a < b)

# <=:小于或等于
# a = 2
# b = 3
# print(a <= b)


# >:大于
# a = 5
# b = 6
# print(a > b)

# >=:大于或等于
# a = 7
# b = 8
# print(a >= b)

# ==: 判断左右两边是否相等
# a = 9
# b = 10
# print(a == b)


# != :判断左右两边是否 不等于
# a = 11
# b = 12
# print(a != b)


# is 判断两个数据的id是否相等(和存储地址相关)
# a = 1
# b = a
# print(a == b)

# print(id(a))
# print(id(b))
# print(id(a) == id(b))

# print(a is b)  # id(a) == id(b)


# a = 1
# b = 1
# print(a == b)
# print(a is b)


# 特殊案例:涉及可变于不可变类型数据,暂时不用理解,记住有这种情况即可
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)


# a = 1
# b = 2
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)


# is not 判断两个对象的id是否不相等(和存储地址相关)
# a = 1
# b = a
# print(id(a))
# print(id(b))
# print(a is not b)


# a = 1
# b = 2
# print(id(a))
# print(id(b))
# print(a is not b)


# == 和 is 的区别
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)


# a = 1
# b = a
# print(a == b)
# print(id(a))
# print(id(b))
# print(a is b)


# print(1 == 2)
# print(1 is 2)








