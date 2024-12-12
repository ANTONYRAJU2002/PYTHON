print("Name : Antony raju\nRoll No : 15")

class BankAccount:
    def __init__(self, AccNo, AccName, AccType, AccBalance=0):
        self.number = AccNo
        self.Name = AccName
        self.Atype = AccType
        self.Balance = AccBalance

    def withdraw(self, Amount):
        if Amount > self.Balance:
            print("Insufficient balance")
        else:
            self.Balance -= Amount

    def deposit(self, Amount):
        self.Balance += Amount

    def display(self):
        print("\nAccount Information:")
        print("Account Number:", self.number)
        print("Account Name:", self.Name)
        print("Account Type:", self.Atype)
        print("Account Balance:", self.Balance)


def main():
    try:
        accno = int(input("Enter your account number: "))
        name = input("Enter your Name: ")
        obj = BankAccount(accno, name, "Savings")
        print("\n1. Account Info")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        while True:
            try:
                opt = int(input("Select your option: "))

                if opt == 1:
                    obj.display()
                elif opt == 2:
                    dep = float(input("Enter the amount to deposit: "))
                    if dep <= 0:
                        print("Deposit amount must be greater than 0.")
                    else:
                        obj.deposit(dep)
                        print(f"Deposited {dep}. Updated balance: {obj.Balance}")
                elif opt == 3:
                    wid = float(input("Enter the amount to withdraw: "))
                    if wid <= 0:
                        print("Withdrawal amount must be greater than 0.")
                    else:
                        obj.withdraw(wid)
                        print(f"Withdrew {wid}. Updated balance: {obj.Balance}")
                elif opt == 4:
                    print("Exiting...")
                    break
                else:
                    print("Invalid option, please select a valid option (1-4).")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    except ValueError:
        print("Invalid account number input! Please enter a valid number.")
main()