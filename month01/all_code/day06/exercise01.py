"""
    画出下列代码内存图
"""
name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
name = "无忌哥哥"
# names[0] =  "敏儿"
# names =  "敏儿"
tuple01[2][0] = "敏儿"
print(tuple01) # ?