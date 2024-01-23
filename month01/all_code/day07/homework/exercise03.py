"""
    在数字列表中查找最大的数字
    算法：
        [170  ,  160  ,  180  ,  165]
    假设第一个就是最大值
    使用假设的和第二个进行比较, 发现更大的就替换假设的
    使用假设的和第三个进行比较, 发现更大的就替换假设的
    使用假设的和第四个进行比较, 发现更大的就替换假设的
    最后，假设的就是最大的.
"""
list01 = [170, 160, 180, 165]
max_value = list01[0]
for i in range(1, len(list01)):  # 1 2 3
    if max_value < list01[i]:
        max_value = list01[i]
print(max_value)

print(max(list01))
