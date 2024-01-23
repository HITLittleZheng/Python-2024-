"""
    练习：一家公司有如下岗位：
     "经理"："曹操","刘备","孙权"
     "技术" ："曹操","刘备","张飞","关羽"
      1. 定义数据结构,存储以上信息.
      2. 是经理也是技术的都有谁?
      3. 是经理不是技术的都有谁?
      4. 不是经理是技术的都有谁?
      5. 身兼一职的都有谁?
      6. 公司总共有多少人数?
"""
dict_person = {
    "经理": {"曹操", "刘备", "孙权"},
    "技术": {"曹操", "刘备", "张飞", "关羽"}
}
print(dict_person["经理"] & dict_person["技术"])
print(dict_person["经理"] - dict_person["技术"])
print(dict_person["技术"] - dict_person["经理"])
print(dict_person["技术"] ^ dict_person["经理"])
print(len(dict_person["技术"] | dict_person["经理"]))
