"""
    画出下列代码内存图
        列表创建
            定位
"""
list01 = ["悟空", "八戒", "唐僧"]
list02 = list01 # list01将列表地址赋值给list02
list01[0] = "孙悟空"

list03 = list01[:] # 创建一份新列表赋值给list03
list01[1] = "猪八戒"

print(list02)  # ["孙悟空","猪八戒","唐僧"]
print(list03)  # ["孙悟空","八戒","唐僧"]
