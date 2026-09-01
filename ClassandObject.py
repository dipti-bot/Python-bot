class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            userinput = input("""Hi, how can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Press 5 to deposit
6. Press 6 to exit
""").strip()

            if userinput == "1":
                self.CreatePin()
            elif userinput == "2":
                self.Changepin()
            elif userinput == "3":
                self.check_balance()
            elif userinput == "4":
                self.withdraw()
            elif userinput == "5":
                self.add_balance()
            elif userinput == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.\n")

    def CreatePin(self):
        if self.pin != '':
            print("Pin already exists.")
            return

        input_pin = input("Enter the pin: ")
        self.pin = input_pin
        input_balance = int(input("Enter balance: "))
        self.balance = input_balance
        print("Pin created successfully")

    def Changepin(self):
        if self.pin == '':
            print("Please create a pin first.\n")
            return

        oldpin = input("Enter old pin: ")
        if self.pin == oldpin:
            newpin = input("Enter new pin: ")
            self.pin = newpin
            print("Pin updated successfully\n")
        else:
            print("Invalid old pin\n")

    def check_balance(self):
        if self.pin == '':
            print("Please create a pin first.\n")
            return

        input_pin = input("Enter the pin: ")
        if input_pin == self.pin:
            print("Your balance is", self.balance, "\n")
        else:
            print("Invalid pin\n")

    def add_balance(self):
        if self.pin =='':
            print("Please create a pin first.\n")
            return
        input_pin = input("Enter the pin:")
        if input_pin == self.pin:
            amount = int(input("Enter the amount : "))
            self.balance += amount
            print("Your amount is : ",self.balance,"\n")
        else:
            print("Invalid pin\n")

    def withdraw(self):
        if self.pin == '':
            print("Please create the pin first\n")
            return
        input_pin = input("Enter the pin: ")
        if input_pin == self.pin:
            if self.balance >0 :
                input_amount = int(input("Enter the amount : "))
                if input_amount <= self.balance:
                    print("Please collect your cash : ",input_amount)
                    self.balance = self.balance- input_amount
                    print("Your remaining balance is : ",self.balance,"\n")
                else:
                    print("Insufficient balance\n")
            else:
                print("Your balance is zero, please deposit first\n")
        else:
            print("Invalid pin\n")
                     


    

obj = Atm()  # object can access the things are present in class



