class Employee:
    name = None # Instance VARIABLE
    age = None
    ph_num = None
    address = None
    email_id = None
    def __init__(self, name, age,ph_num,address,email_id):
        print("Called, Object is created")
        self.name = name
        self.age = age
        self.ph_num = ph_num
        self.address = address
        self.email_id = email_id

    def print_emp_details(self):
        print("Employee Details")
        print("Name-", self.name)
        print("age-",self.age)
        print("Ph_num-", self.ph_num)
        print("address-",self.address)
        print("mailid-",self.email_id)

emp1 = Employee(input("enter name"),input("age"), input("Ph_num"),input("address"),input("mailid"))

emp2 = Employee(input("enter name"),input("age"), input("Ph_num"),input("address"),input("mailid"))

emp3 = Employee("Surya", 30, 9494552084, "AP", "suryanadh@gmail.com")

emp1.print_emp_details()
emp2.print_emp_details()
emp3.print_emp_details()
