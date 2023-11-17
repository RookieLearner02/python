"""

Inheritance

Dont Repeat Yourself

"""


class Employee:
    """

    Employee's Information Class

    """
    bonus = 2000
    total_employees = 0
    def __init__(self, name, emp_num, salary):
         self.name = name
         self.emp_num = emp_num
         self.salary = salary
         Employee.total_employees += 1
    
    def get_employee_info(self):
         return 'Employee: ' + self.name + '\n' \
                'Emp #' + str(self.emp_num) + '\n' \
            

    def add_bonus_to_salary(self):
          salary_bonus = int(self.salary + self.bonus)
          return 'Employee Name: ' + self.name + '\n' \
                 ' Salary + Bonus: ' + str(salary_bonus) + '\n'
    

class Developer(Employee):
    def __init__(self, name, emp_num, salary, lang):
          self.lang = lang
          super().__init__(name, emp_num, salary)
    def develop_applications(self):
         return 'Develop Application'


class Tester(Employee):
    def __init__(self, name, emp_num, salary, web_mobile):
          self.web_mobile = web_mobile
          Employee.__init__(self, name, emp_num, salary)
    def test_application(self):
     return 'Test Applications'


emp1 = Developer('Developer Srisha', 12, 120000, 'Java')

emp2 = Employee('Employee Doe', 13, 110000)

emp3 = Tester('Srisha Joshi', 14, 100000, 'Web')

print('Employee 12 is a', emp1.lang,'Developer')


print(emp1.add_bonus_to_salary())
print(emp2.add_bonus_to_salary())

print('Employee 14 is a', emp3.web_mobile, 'Tester')


'''
Multiple Inheritance

&

Multi level Inheritance

'''

class Automation_Engineer(Tester, Developer):
    def __init__(self, name, emp_num, salary, lang, web_mobile):
        super().__init__(name, emp_num, salary, lang)
        Tester.__init__(self, name, emp_num, salary, web_mobile)

    def get_employee_info(self):
         return 'Employee: ' + self.name + '\n' \
                'Emp #' + str(self.emp_num) + '\n' \
                'Employee Salary : $' + str(self.salary) + '\n' 

automation = Automation_Engineer('Srisha B Joshi', 15, 105000, 'python', 'mobile')

employee = Employee('joshi', 17, 1200)

print(automation.get_employee_info())
print(employee.get_employee_info())

'''

-- POLYMORPHISM

'''

