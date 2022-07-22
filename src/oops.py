class Employee:
    def __init__(self,name,id_num,emp_type,department,designation,salary):
        """This functions takes the employee details as the input"""
        self.name=name
        self.id_num=id_num
        self.emp_type=emp_type
        self.department=department
        self.designation=designation
        self.salary=salary
    def show(self):
        """This function displays the employee details"""
        print("Name of the employee:", self.name)
        print("ID:",self.id_num)
        print("Employee tye:",self.emp_type)
        print("Department:",self.department)
        print("Designation:",self.designation)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,id_num,emp_type,department,designation,salary,num_emp,reporting_to):
        """This function takes the managers details as the input"""
        super().__init__(name,id_num,emp_type,department,designation,salary)
        self.num_emp=num_emp
        self.reporting_to=reporting_to
    def show_manager_details(self):
        """This function displays the manager details"""
        super().show()
        print("Number of employees:",self.num_emp)
        print("Reporting to:",self.reporting_to)

employee_details={}
manager_details={}
i=0
j=0
print("enter the details of employee or Manager")
print("press \"Q\" to stop..!\n")
while True:
    name=input("enter the name of the employee: ")
    idnum=int(input("employee id num: "))
    emptype=input("employee type: ")
    department = input("department name: ")
    designation = input("designation: ")
    salary = int(input("salary: "))
    if "manager" in designation:
        numemp=int(input("number of employees: "))
        reportingto=input("repoter name: ")
        m1=Manager(name,idnum,emptype,department,designation,salary,numemp,reportingto)
        #print("\n\tDetails of manager \n--------------------------------------")
        #m1.show_manager_details()
        #print("--------------------------------------\n")
        manager_details[f"m{i}"]=m1
        i+=1
    else:
        e1=Employee(name,idnum,emptype,department,designation,salary)
        #print("\n\tEmployee Details \n--------------------------------------")
        #e1.show()
        #print("--------------------------------------\n")
        employee_details[f"e{j}"]=e1
        j+=1
    if input().lower()=="q":
        break
print("\tEmployee details: \n----------------------------------------------------\n")
for num in range(0,i):
    employee_details[f'e{num}'].show()
    
print("\n======================================================\n")
print("\tManager details: \n----------------------------------------------------\n")
for num in range(0,j):
    manager_details[f'm{num}'].show_manager_details()