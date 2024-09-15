#project  usig oops. create bank atm machine"""
""""""
# class Atm:
#     def __init__(self):
#         self.pi=n ''
#         self.balance  =0
#         self.menu()

#     def menu(self):
#         use_input =input("""how would you like to proceed::
#                          1. press 1 to set the print
#                          2. press 2 to deposit
#                          3.press 3 to withdraw
#                          4.press 4 to check balance
#                          5. press 5 to exit 
#                                              -----:""")
#         if use_input=='1':
#             self.set_pin()
#         elif use_input =='2':
#             self.deposit()
#         elif use_input =='3':
#             self.withdraw()
#         elif use_input=='4':
#             self.check_balance()
#         elif use_input =='5':
#             print("exiting..........................................................................................")
        
#         else:
#             print("invalid input pls try again below..................................................................")

#         self.menu()
    
#     def set_pin(self):
#         self.pin =input("enter the pin:")
#         print("pin set succesful......................................................................................")
#         self.menu()
     

#     def deposit(self):
#         temp =input("enter the pin:")
#         if temp == self.pin:
#             amount =float(input("ente the amount:"))
#             self.balance  =self.balance +amount
#             print(f"deposit of Rs:{amount} is succesful...................................................................")
#         else:
#             print("enetred pin is invald..................................................................................")
#         self.menu()

#     def withdraw(self):
#         temp = input("enter the pin:")
#         if temp == self.pin:
#             amount =float(input("enter the amount:"))
#             if amount<= self.balance:
#                 self.balance =self.balance-amount
#                 print(f"withdraw of Rs:{amount} is succesful..................................................................")
#             else:
#                 print("balance is insufficiant")
#         else:
#             print("invali pin:..................................................................................................")
#         self.menu()
        
        
#     def check_balance(self):
#         temp= input("enetr teh pin:")
#         if temp == self.pin:
#             print("your current balance is :",self.balance)
#         else:
#             print("invalid pin.....................................................................................................")
#         self.menu()
       




# sbi =Atm()
        

#prject 2 IRCTC

# import requests   
# class IRCTC:
#     def __init__(self):
        # user_input =input("""how would like to proceed:................
#                           1. press 1 for live running status:
#                           2. press 2 for PNR status:
#                           3. press 3 for train shedule:....:""")
#         if user_input =='1':
#             pass
#         elif user_input =='2':
#             pass
#         elif user_input =='3':
#             self.train_shedule()
#         else:
#             print("entery is invalid")

#     def train_shedule(self):
#         train_no = input("enter the train number----:")
#         self.fetch_data(train_no)
#     def fetch_data(self,train_no):
#         data = requests.get("http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/{}.format(train_no)")

#         data =data.json()
        
#         print(data['Route'])


# obj =IRCTC()
# """







