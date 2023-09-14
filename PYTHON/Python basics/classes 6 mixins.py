
# Employee superclass
class Employee:
    """
    Base class for employees
    """
    # class attribute
    employee_no = 0

    def __init__(self, name, no_of_years):
        # instance attribute
        self.name = name
        self.no_of_years = no_of_years
        Employee.employee_no += 1
        self.employee_no = Employee.employee_no

    def details(self):
        """
        Method to return employee details as a string
        """
        return f"Name: {self.name}\n Years Worked: {self.no_of_years}\n Employee Number: {self.employee_no}\n"

# HolidatMixin - a method that can be used by several classes
class HolidayMixin:
    """
    Mixin to calculate holiday entitlement by years of service.
    Note that a mixin has no __init__ as you cannot create an instance of a mixin
    """
    def calculate_holidays(self, no_of_years):
        """
        Method that returns holidays as an integer if given no of years of service
        """
        BASE_HOLIDAY = 20
        bonus = 0
        holidays = BASE_HOLIDAY
        if no_of_years < 3:
            bonus = holidays + 1
        elif no_of_years <= 5:
            bonus = holidays + 2
        elif no_of_years > 5:
            bonus = holidays + 3
        return f'Holidays: {bonus}'

# subclass of Holiday and Employee
class DirectDeveloper(HolidayMixin, Employee):
    """
    Class for direct developer employee inheriting from 
    Employee class but also inheriting from HolidayMixin
    """
    def __init__(self, name, no_of_years, prog_lang):
        self.prog_language = prog_lang
        Employee.__init__(self, name, no_of_years)

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

    def get_details(self):
        """
        Method to return direct developer details as a string
        Uses details() method inherited from Employee super class
        """
        return Employee.details(self) + f'Programming Language: {self.prog_language}'


eric = DirectDeveloper("Eric Praline", 2, "python")

# Prints out all the attributes of your eric instance using get_details method from DirectDeveloper
# If you use the details method from Employee then the Programming Language will not print
print(eric.get_details())
# The mixin method is usable for instance eric
print(eric.calculate_holidays(eric.no_of_years))
# Uses the calculate_salary method from DirectDeveloper
print(f'${eric.calculate_salary()}')

luigi = DirectDeveloper("Luigi Vercotti", 10, "php")
print(luigi.get_details())
print(luigi.calculate_holidays(luigi.no_of_years))
print(f'${luigi.calculate_salary()}')
