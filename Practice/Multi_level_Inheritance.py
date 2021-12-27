class Parent:
    def assign_name(self,name):
        self.name=name

    def show_name(self):
        return self.name

class Child(Parent):
    def assign_age(self,age):
        self.age=age

    def show_age(self):
        return self.age

class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender=gender

    def show_gender(self):
        return self.gender

c1=GrandChild()
c1.assign_name("Vikas")
c1.assign_age(24)
c1.assign_gender("Male")

print(c1.show_name())
print(c1.show_age())
print(c1.show_gender())