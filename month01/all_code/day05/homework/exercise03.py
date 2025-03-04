"""
6. 一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)   13 次
    -- 全过程总共移动多少米?
    数据：高度       次数     距离
    处理：高度/=2   次数+=1  距离+=?
"""
height = 100
count = 0
distance = height
while height / 2 > 0.01:
    # 弹起来
    height /= 2
    count += 1
    distance += height * 2 # 累加height起落距离
    print(f"第{count}次弹起来的高度是{height}")
print(f"总共弹起来{count}次")
print(f"总共移动{distance:.2f}米")