from functools import reduce
# 导入 reduce() 函数

iterable = range(200, 1001)
# 生成一个 range() 对象，内容为集合 { x in Z | x in (200, 1000) } 
# 即 200 到 1000 包括 1000 在内的正整数

multi_three = reduce(lambda x, y : x * y, filter(lambda i: i % 3 == 0, iterable))
# 利用 lambda 匿名函数进行计算
# 利用 filter 筛选出能被 3 整除的数
# 再利用 reduce 累乘这些数
# 最后得出结果

print(multi_three)
# 输出答案