# 1.请用索引的方式将列表中'abcd' 与 '上山打老虎' 2个元素位置互调
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]  
a[3] = "上山打老虎"
a[-1] = 'abcd'
print(a)

print('\n')
# 2.请将该列表中的元素,分为2个不同类型(分别是数字类型和字符串类型)分别保存到2个不同的列表当中,用代码实现
a = [1, 2, 3.3, 'abcd', 5, "上山打老虎"]
b_number = []     # 数字类型
c_str = []        # 字符串类型
for x in a:
    if type(x) == int or type(x) == float:
        print(x,type(x))
        b_number.append(x)
    elif type(x) == str:
        print(x,type(x))
        c_str.append(x)
print(b_number)
print(c_str)









