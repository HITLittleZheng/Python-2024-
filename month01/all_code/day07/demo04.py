"""

"""
# 商品信息
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 1. 打印所有商品信息,
# ​	   格式：商品编号xx,商品名称xx,商品单价xx.
for key, value in dict_commodity_infos.items():
    print("商品编号%s,商品名称%s,商品单价%s." % (key, value["name"], value["price"]))
# 2. 打印所有订单中的信息,
#    格式：商品编号xx,购买数量xx.

#
# 3. 打印所有订单中的商品信息,
#    格式：商品名称xx,商品单价:xx,数量xx.