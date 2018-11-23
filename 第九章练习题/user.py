class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")
        
    def increment_login_attempts(self):
              """增加login_attempts的值"""
              self.login_attempts += 1

    def reset_login_attempts(self):
              """将login_atempts的值重置为0"""
              self.login_attempts = 0


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
