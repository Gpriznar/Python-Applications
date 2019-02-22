class User:
    def __init__(self,first_name,last_name,age,city,state,login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.state = state
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.city, self.state)

    def greet_user(self):
        print(f"Hello " + self.first_name + ", " + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts +=1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

user = User("Gregory", "Priznar", "31", "Houston", "Texas", 0)
user.greet_user()
user.describe_user()
user.print_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()

user1 = User("Mary", "Jane", "21", "San Diego", "California", 0)
user1.greet_user()
user1.describe_user()

user2 = User("Lauren", "Gerold", "34","Houston" ,"Texas", 0)
user2.greet_user()
user2.describe_user()

user3 = User("James", "Bond", "45", "London", "England", 0 )
user3.greet_user()
user3.describe_user()
