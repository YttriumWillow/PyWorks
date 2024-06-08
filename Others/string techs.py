s = ''
s.capitalize()
# 将字符串的第一个字符转换为大写
s.title()
# 将字符串的所有单词第一个字符转换为大写
count(str, beg= 0,end=len(string))
# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
endswith(suffix, beg=0, end=len(string))
# 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False
find(str, beg=0, end=len(string))
# 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含'''''''返回开始的索引值'''''''，否则返回-1
index(str, beg=0, end=len(string))
# 跟find()方法一样，只不过如果str不在字符串中会报一个异常
islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isbigger()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
'?'.join(seq)
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
'?'.split(seq)
# 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)拆开为一个新的列表
max(str)
# 返回字符串 str 中最大的字母
min(str)
# 返回字符串 str 中最小的字母
replace(old, new [, max])
# 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次
lstrip()
# 截掉字符串左边的空格或指定字符
rstrip()
# 删除字符串字符串末尾的空格
strip() 
# 在字符串上执行 lstrip()和 rstrip()
