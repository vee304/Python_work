
class User:
    def __init__(self, user_email, name, password, current_job):
        self.email = user_email
        self.name = name
        self.passwd = password
        self.currn_job = current_job

    def change_password(self, new_password):
        self.passwd = new_password

    def change_job_title(self, new_job):
        self.currn_job = new_job

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.currn_job}. You can contact at {self.email}")