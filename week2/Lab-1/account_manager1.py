class AccountManager1:
    def fill_account_data(self, acc):
        acc.acc_no = "004701"
        acc.name = "Nitesh"
        acc.balance = 45000.0

    def display_account_data(self, acc):
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
