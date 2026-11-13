
class Employee:
    """Base class for an employee."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def monthly_pay(self):
        """Returns the monthly pay of the employee."""
        return self.salary


class Manager(Employee):
    """Manager class inheriting from Employee, adding a bonus."""
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def monthly_pay(self):
        """Returns salary plus bonus."""
        return super().monthly_pay() + self.bonus


class Intern(Employee):
    """Intern class inheriting from Employee, with a fixed pay of 300."""
    def __init__(self, name):
        super().__init__(name, 300)

    def monthly_pay(self):
        """Returns fixed intern pay."""
        return self.salary


if __name__ == "__main__":
    print("=== Testing Employees Payroll ===")
    
    team = [
        Employee("Ahmad", 800),
        Manager("Mohammad", 1200, 300),
        Intern("Zaid")
    ]
    
    total_payroll = 0
    for emp in team:
        pay = emp.monthly_pay()
        total_payroll += pay
        print(f"{emp.name} ({type(emp).__name__}) Pay: {pay}")
        
    print(f"Total Payroll: {total_payroll}")