"""
    信息管理系统
"""


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class EmployeeController:
    """
        员工信息控制器：业务逻辑,核心功能
    """

    def __init__(self):
        self.list_employee = []
        self.start_id = 1001

    def add_employee(self, emp):
        """
            添加商品信息
        :param employee:需要添加的商品信息
        """
        # 设置编号
        emp.eid = self.start_id
        self.start_id += 1
        # 存储
        self.list_employee.append(emp)

    def remove_employee(self, eid):
        """
            根据商品编号删除商品信息
        :param cid:商品编号
        :return:是否删除成功
        """
        for i in range(len(self.list_employee)):
            if self.list_employee[i].eid == eid:
                del self.list_employee[i]
                return True
        return False

    def update_employee(self, emp):
        for item in self.list_employee:
            if item.eid == emp.eid:
                item.__dict__ = emp.__dict__
                return True
        return False


class EmployeeView:
    """
        员工信息视图：界面逻辑,输入输出
    """

    def __init__(self):
        self.controller = EmployeeController()

    def display_menu(self):
        print("1 添加员工")
        print("2 显示员工")
        print("3 删除员工")
        print("4 修改员工")

    def select_menu(self):
        item = input("请输入您的选项：")
        if item == "1":
            self.input_employee()
        elif item == "2":
            self.display_employees()
        elif item == "3":
            self.delete_employee()
        elif item == "4":
            self.modify_employee()

    def input_employee(self):
        employee = EmployeeModel()
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))
        self.controller.add_employee(employee)

    def display_employees(self):
        for item in self.controller.list_employee:
            print(item.__dict__)

    def delete_employee(self):
        cid = int(input("请输入员工编号："))
        if self.controller.remove_employee(cid):
            print("删除成功")
        else:
            print("删除失败")

    def modify_employee(self):
        employee = EmployeeModel()
        employee.eid = int(input("请输入员工编号："))
        employee.name = input("请输入员工名称：")
        employee.did = int(input("请输入部门编号："))
        employee.money = int(input("请输入员工工资："))
        if self.controller.update_employee(employee):
            print("修改成功")
        else:
            print("修改失败")


view = EmployeeView()
while True:
    view.display_menu()
    view.select_menu()
