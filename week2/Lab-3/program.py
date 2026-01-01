from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
        # store employee data
        emp.emp_id = "E101"
        emp.emp_name = "Ananya"
        emp.gender = "Female"

        # create address object
        addr = Address()
        addr.address1 = "MG Road"
        addr.address2 = "Near Metro Station"
        addr.city = "Bangalore"
        addr.pincode = "560001"

        # store address inside employee
        emp.address = addr

    @staticmethod
    def show_data(emp):
        # ----------------Display the employee information
        print("Employee Id : ", emp.emp_id)
        print("Employee Name : ", emp.emp_name)
        print("Employee Gender : ", emp.gender)

        print("Employee Address : --------------")
        print("Address 1 : ", emp.address.address1)
        print("Address 2 : ", emp.address.address2)
        print("City : ", emp.address.city)
        print("PinCode : ", emp.address.pincode)
        print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
