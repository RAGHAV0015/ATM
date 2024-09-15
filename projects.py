#prject 2 IRCTC

import requests   
class IRCTC:
    def __init__(self):
        user_input =input("""how would like to proceed:................
                          1. press 1 for live running status:
                          2. press 2 for PNR status:
                          3. press 3 for train shedule:....:""")
        if user_input =='1':
            pass
        elif user_input =='2':
            pass
        elif user_input =='3':
            self.train_shedule()
        else:
            print("entery is invalid")

    def train_shedule(self):
        train_no = input("enter the train number----:")
        self.fetch_data(train_no)
    def fetch_data(self,train_no):
        data = requests.get("http://indianrailapi.com/api/v2/TrainSchedule/apikey/<apikey>/TrainNumber/{}.format(train_no)")

        data =data.json()
        
        print(data['Route'])


obj =IRCTC()








