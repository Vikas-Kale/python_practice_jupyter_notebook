class Employee:

    details=[]

    def __init__(self,name,age,mobile_number,address):
        self.name=name
        self.age=age
        self.mobile_number=mobile_number
        self.address=address

    def show_Info(self):
        Employee.details.append(self.name)
        Employee.details.append(self.age)
        Employee.details.append(self.mobile_number)
        Employee.details.append(self.address)
        print(Employee.details)
    

e1=Employee('Vikas',24,7798743804,'Pune')

e1.show_Info()
