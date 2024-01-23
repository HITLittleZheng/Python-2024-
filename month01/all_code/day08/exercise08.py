"""

"""


# 将函数代码加载到内存的代码区,函数体不执行
def func01(p1, p2):
    p1 = "孙悟空"  # 修改的是栈帧中的变量,不影响a
    p2["八戒"] += 50  # 修改的是传入的字典,影响b

a = "悟空"
b = {"八戒": 100}
# 调用函数在内存中开辟空间(栈帧),存储内部创建的变量.
func01(a, b)
print(a)  # "悟空"
print(b)  # {"八戒": 150}
