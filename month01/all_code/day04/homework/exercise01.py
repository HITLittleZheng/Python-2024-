"""
    电梯设置规定：
        如果承载⼈不超过10⼈，且总重量不超过1000千克，可以正常使⽤，否则提示超载。
    步骤:
        终端中获取人数/总重量
        显示电梯正常运行
            电梯超载
"""

# num = int(input("请输入电梯承载人数:"))
# weight = float(input("请输入电梯承载重量:"))
# if num <= 10 and weight <= 1000:
#     print("电梯正常运行")
# else:
#     print("电梯超载")

if int(input("请输入电梯承载人数:")) <= 10 and \
        float(input("请输入电梯承载重量:")) <= 1000:
    print("电梯正常运行")
else:
    print("电梯超载")