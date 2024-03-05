class User:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        
    def describe_user(self):
        print(f"User의 이름은 {self.first_name}{self.last_name} 성별은 {self.gender}")
        
    def greet_user(self):
        print("반갑습니다.{}{}님".format(self.first_name,self.last_name))
        
class Admin(User):
    
    def __init__(self,first_name, last_name, gender):
        super().__init__(first_name,last_name,gender)
        self.privileges = ['can delete post','can add post','can ban user']
        
    def show_privileges(self):
        print("관리자 권한을 출력합니다.")
        for privileges in self.privileges :
            print(privileges)
    

my_user = User('신','건영','남')
my_Admin = Admin('김','보성','남')

my_Admin.describe_user()
my_Admin.show_privileges()

print(my_user)
my_user.describe_user()
my_user.greet_user()
