class SalaryCalculator:

    @staticmethod
    def get_salary(emp):
        allowance = SalaryCalculator.get_allowance(emp)
        salary = emp.basic + emp.hra + allowance
        return salary

    @staticmethod
    def get_allowance(emp):
        allowance = emp.basic * emp.allowance_percentage / 100.0
        return allowance
