class Parent1:
    def assign_str_one(self,str_one):
        self.str_one=str_one

    def show_str_one(self):
        print(f"The value of str one:- {self.str_one}")

class Parent2:
    def assign_str_two(self,str_two):
        self.str_two=str_two

    def show_str_two(self):
        print(f"The value of str_two is {self.str_two}")

class Derived(Parent1,Parent2):
    def assign_str_three(self,str_three):
        self.str_three=str_three

    def show_str_three(self):

        print(f"I am in Derived class.\nThe value of str three is {self.str_three}")

c1=Derived()
c1.assign_str_one("One")
c1.assign_str_two("Two")
c1.assign_str_three("Three")

c1.show_str_one()
c1.show_str_two()
c1.show_str_three()
