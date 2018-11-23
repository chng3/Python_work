# 9-12 多个模块

from user1 import User

class Privileges():
        """存储管理员权限的类"""
        def __init__(self, privileges=[]):
                self.privileges = privileges

        def show_privileges(self):
                """显示管理员的权限"""
                print("\nPrivileges:")
                if self.privileges:
                        for privilege in self.privileges:
                                print("- " + privilege)
                else:
                        print("- This user has no privileges.")


class Admin(User):
        """具有管理权限的用户"""
        def __init__(self, first_name, last_name, username, email, location):
                """初始化管理员属性"""
                super().__init__(first_name, last_name, username, email, location)
                self.privileges = Privileges()
