"""
数据结构: 又可以被称为容器,因为这些数据类型 是有着一定结构的组合.(本质上也是数据类型)
列表,集合,元组,字典 是Python内置的4种数据结构(数据类型).
"""
# 列表
# a = [1, 2, 3, 4, 5, 6]  # list
# print(a)
# print(type(a))

# 元组
# b = (1, 2, 3, 4, 5, 6)  # tuple
# print(type(b))

# 集合
# c = {1, 2, 3, 4, 5, 6}  # set
# print(type(c))

# 迭代循环列表a
# for i in a:
#     print(i)

# 迭代循环元组b
# for i in b:
#     print(i)

# 迭代循环集合c
# for i in c:
#     print(i)


# 被称之为数据结构,说明其组成更加灵活
# 几乎可以放任何形式的数据类型
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎", [1, 2, 3], 10]

# for i in a:
    # print(i)
    # print(type(i))

# 因为数据结构中的元素个数不相同,所以也有长度的概念
# 我们可以通过len()函数计算长度
# print(len(a))


"""
列表
"""
# 怎么去表达每个元素的位置?
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]  # 有序
# print(a)
# 索引:从0开始

# 索引: 0  1   2     3     4     5
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]

# 1.索引取值:使用取索引的方式取列表里的对应值
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a)
# 如果输出超过最大索引值的数字会怎么样?
# print(a[6])

a = []
# print(type(a))
# print(bool(a))
# print(a[0])  # 报错

# for i in a:
#     print('哈哈')


# 2.通过某个列表中的元素的值 取到对应的索引号
# 使用: 列表名.index(元素) 方法可以获取到指定列表的指定元素的索引
# 例如:a 列表中 的 'abcd'元素的索引号
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]

# print(a.index('abcd'))  # a[3]


# 3.通过for循环,依次全部取出
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# for i in a:  # 依次拿到列表当中的每个元素
#     print(i, a.index(i))  # 索引与元素本身 一一对应 打印输出


# 嵌套列表取值：
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎", [1, 2, 3], 10]
# print(a[6])
# print(a[6][1])


"""
列表的切片操作: 分段式取值
"""
#    0  1   2     3     4     5
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]

# print(a[1:3])

# print(a[3])
# print(a[3:4])
# 因为0表示从开头进行截取，所以是可以省去的
# print(a[0:3])
# 简写的模式，同a[0:3]
# print(a[:3])
# 如果列表要截到最后,也是可以省去的
# print(a[1:5])
# print(a[1:6])
# print(a[1:])
# print(a[:])

# print(a[1:len(a)])  # 7   1-6   10   0-9
# 简写的模式，同a[1:6]
# print(a[1:])

# 考题
# print(a[:])

# 当需要取出第二个元素到第五个元素到特定数据时
# print(a[1:5])
# 因为索引都是从0开始的，且这个选定的范围是包头去尾的，
# 所以第二个元素的索引是1，而第五个元素的索引是4，我们则需要取到5


# 步长
# 在第二个元素到第五个元素中间,每2个元素取第1个
#    0  1   2     3     4     5
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# print(a[1:5])
# print(a[1:5:2])  # 1 , 2 , 3 , 4
# print(a[2:5])
# print(a[2:5:2])
# print(a[1:4:2])  # 1 , 2 , 3

# 思考:如果步长为1,是什么效果?

# 同样的操作，我们可以倒叙取值，
# 例如最后一个元素
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# print(a[-1])
# 取最后两个元素
# print(a[-2:-6:-1])
# print(a[4:1:-1])
# print(a[1:-1:1])
# print(a[:3:-1])
# 因为我们都是假定不知道列表的长度，所以最后的索引直接可以省去


"""
列表的数据添加
"""
# 1.append() 添加
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a.append(4)
# print(a)
# append()这里的添加数据是指将数据作为一个元素直接添加到原来的列表中的最后面


# 2.extend() 拓展
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a.append([6, 7])
# print(a)

# 等价关系
# for i in [6, 7]:  # a.extend([1,2,3])
#     a.append(i)
#
# print(a)

# b = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# b.extend([6, 7])
# print(b)
# b.extend(['lalala', 7])
# print(b)
# extend()添加进来的列表不再是以列表的形式保存在a中了，
# 而是将每一个元素单独作为数据保存在原有列表中

# 3.insert():数据的插入，指定数据插入在列表的哪一个索引的位置。
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# 在索引为4的位置插入数据'哈哈哈哈'
# a.insert(4, '哈哈哈哈')
# print(a)
# 在索引为4的位置插入列表
# a.insert(4, [2, 3])
# print(a)


"""
列表数据的修改
"""
# 可以直接通过指定列表的索引来修改对应的值
lyst = ['大娃', '二娃', '三娃', '四娃', '五娃', '六娃', '七娃']
# lyst[3] = '蝎子精'
# print(lyst)

# 通过切片操作，我们甚至能批量修改
# lyst[3:6] = ['爷爷', '大妖怪', '小妖怪', '蛇精']
# lyst[3:6] = [1, 2, 3, 4]
# print(lyst)

"""
列表数据的删除
"""
# 1.pop():可以将列表里的数据剔除并返回出来
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# c = a.pop()
# print(c)
# print(a)

# 再执行一次呢?
# print(a.pop(2))
# print(a)
# pop()默认删除最后一个元素

# 2.clear():一键清除所有元素
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a.clear()
# print(a)
# print(type(a))

# del a
# print(a)


# remove()
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a.remove('abcd')
# print(a)


"""
列表的排序
"""
# sort()方法
a = [1, 2, 5, 6, 3, 9]
# print(a)
# print(id(a))
# a.sort()
# print(a.sort())
# print(a)
# print(id(a))

# 如果数据类型不同呢?
# a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
# a.sort()
# print(a)

# 当列表里都是字符串时(也是可以排序的)
# a = ['2', '5', 'a', 'd', 'ab', 'ac']
# a.sort()
# print(a)

# ord()函数的作用:
# print(ord('2'))
# print(ord('5'))
# print(ord('a'))
# print(ord('d'))
# print(ord('ab'))
# print(ord('ac'))

"""
字符串的比较是依据字符对应的 ASCII 数值或者 Unicode 数值,
从小到大依次排列,当字符串中存在多个字符时，会优先比较第一个，
第一个相同时会比较第二个，以此类推，直到确定顺序的大小。
我们可以通过ord()函数测试一下:
ord()函数以一个字符串（Unicode 字符）作为参数，
返回对应的 ASCII 数值或者 Unicode 数值.
"""

# 排序不仅可以从小到大,也可以从大到小(reverse参数)
# a = [9, 21, 3, 6, 5.5, 10, 1.9, 0]
# a.sort(reverse=False)
# print(a)

# a = ['2', '5', 'a', 'd', 'ab', 'ac']
# a.sort(reverse=False)
# print(a)

# reverse() 函数:直接反转列表(区别?)
# a = [9, 21, 3, 6, 5.5, 10, 1.9, 0]  # a[::-1]
#
# a.reverse()
# print(a)

# print(a[:3:-1])  # 是从左往右还是从右往左,取决于步长方向
# print(a[::-1])


# 补充内容:
# 字符串join方法的使用
# a = '-'
# c = a.join(['Hello', 'world', '哈哈哈哈哈哈'])
# print(c)  # 输出: 'Hello world 哈哈哈哈哈哈'
# print(type(c))
# d = []
# d.append(c)
# print(d)


# 字符串替换:replace
# a = 'hello world 哈哈哈哈哈哈'
# b = a.replace(' ', '', 2)  # 第1个参数:原字符串中被替换的内容 第2个参数:新替换的内容 第3个参数:从左往右替换的次数(不填默认全部替换)
# print(b)
# print(a)

# 字符串切割:split
# a = 'hello world 哈哈哈哈哈哈'
# b = a.split(' ', 2)  # 第1个参数:字符串中被切割的字符 第2个参数:从左往右切割的次数
# print(b)

# 错误写法
# a = [1, 2, 3]
# b = [1, 2, 3]
# a.append(b)
# print(a)

# 如果再给a添加个元素1
# a.append(1)
# print(a)
# for i in a:
#     print(i)