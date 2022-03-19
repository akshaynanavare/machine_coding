import sys
from user import User

class Expenses:
    def __init__(self) -> None:
        self.UserPool = {}
        self.UserCount = 0
    
    def addExpenses(self,own,pay,amount):
        owner = None
        payer = None
        if own in self.UserPool.keys():
            owner = self.UserPool[own]
        else:
            owner = User(own)
            self.UserPool[own] = owner
            self.UserCount +=1
        
        if pay in self.UserPool.keys():
            payer = self.UserPool[pay]
        else:
            payer = User(pay)
            self.UserPool[pay] = payer
            self.UserCount +=1

        owner.updateYouOwn(pay,amount)
        payer.updateTheyOwn(own,amount)

    def processExact(self,owner,no_of_users,users,amounts):
        for i in range(no_of_users):
            self.addExpenses(owner,users[i],int(amounts[i]))

    def processEqual(self,total_amount,owner,no_of_users,users):
        amount = total_amount/no_of_users
        for i in range(no_of_users):
            if owner == users[i]:
                continue
            self.addExpenses(owner,users[i],amount)

    def processPercent(self,owner,total_amount,no_of_users,users,amounts):
        for i in range(no_of_users):
            amount = int(amounts[i])*total_amount/100
            if owner == users[i]:
                continue
            self.addExpenses(owner,users[i],amount)

    def processInputs(self):
        while True:
            txt = input("Enter expense : ")
            inputs = txt.split(" ")
            if inputs[0] == "EXPENSE":
                owner = inputs[1]
                total_amount = int(inputs[2])
                no_of_users = int(inputs[3])
                users = inputs[4:4+no_of_users]
                method = inputs[4+no_of_users]
                if method == "EXACT":
                    amounts = inputs[5+no_of_users:]
                    self.processExact(owner,no_of_users,users,amounts)
                elif method == "EQUAL":
                    self.processEqual(total_amount,owner,no_of_users,users)
                elif method == "PERCENT":
                    amounts = inputs[5+no_of_users:]
                    percent = 0
                    for i in amounts:
                        percent += int(i)
                    if percent != 100 :
                        print("Invalid percent")
                        continue
                    self.processPercent(owner,total_amount,no_of_users,users,amounts)             
                else:
                    print("Method not allowed")

            if inputs[0]  == "SHOW" :
                if len(inputs) > 1 :
                    user_id = inputs[1]
                    if not user_id in self.UserPool.keys():
                        continue
                    userObj = self.UserPool[user_id]
                    for key in userObj.theyOwn.keys():
                        msg = "%s owes %s : %d" %(user_id , key , userObj.theyOwn[key])
                        print(msg)
                    for key in userObj.youOwn.keys():
                        msg = "%s owes %s : %d" %(key , user_id , userObj.youOwn[key])
                        print(msg)
                else :
                    for user in self.UserPool.values():
                        for key in user.youOwn.keys():
                            msg = "%s owes %s : %d" %( key, user.id , user.youOwn[key])
                            print(msg)
            if inputs[0]  == "EXIT" :
                sys.exit()


expense = Expenses()
expense.processInputs()

        