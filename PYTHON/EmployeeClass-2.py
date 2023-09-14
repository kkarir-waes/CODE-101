class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, fname, sname, no_of_years):
        # instance attribute
        self.fname = fname
        self.sname = sname
        self.no_of_years = no_of_years
        Employee.employee_no +=1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"First Name: {self.fname}\n Surname: {self.sname}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"

class ExternalContract:
    """
    Class for contract employees
    """

    def __init__(self, contract_cost):
        self.contract_cost = contract_cost

    def cost(self):
        """
        Returns the contract cost added to the salary
        """
        return self.contract_cost + 30000


class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    """
    def calculate_holidays(self, no_of_years):
        """
        Returns holidays as an integer
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if self.no_of_years < 3:
            bonus = holidays + 1
        elif self.no_of_years <= 5:
            bonus = holidays + 2
        elif self.no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'


class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class. 
    """
    def __init__(self, fname, sname, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, fname, sname, no_of_years)

    def calculate_salary(self):
        """
        Returns salary plus bonus as an integer
        """
        base = 30000
        if self.prog_language.lower() == 'python':
            bonus = base * 0.10
        else:
            bonus = 0
        return base + bonus

    def details(self):
        """
        Method to return direct developer details as a string
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


class ContractDeveloper(HolidayMixin, Employee, ExternalContract):
    """
    Class is subclass of Employee, composition relationship
    with ExternalContract and using HolidayMixin
    """
    def __init__(self, fname, sname, no_of_years, prog_language, contract_cost):
        self.prog_language = prog_language
        self.contract_cost = contract_cost
        Employee.__init__(self, fname, sname, no_of_years)   

    def details(self):
        """
        Returns inherited details plus contract cost
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}\n Contract cost: {ExternalContract.cost(self)}'


dev = DirectDeveloper("Eric", "Praline", 2, "python")
# There is no composition relationship here. A DirectDeveloper is an Employee
print(dev.details())
print(dev.calculate_holidays(dev.no_of_years))
print(f'${dev.calculate_salary()}')

contractor = ContractDeveloper("Luigi", "Vercotti", 10, "python", 100000)
# When the contractor details are printed the Contract cost is obtained from ExternalContract class
# There is a composition relationship as contractor has an ExternalContract
# However, an external contract is not an employee
# ExternalContract is an object that could be reused by many other objects. 
print(contractor.details())
# The mixin can also be used
print(contractor.calculate_holidays(contractor.no_of_years))



