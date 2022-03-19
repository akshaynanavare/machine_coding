

class User:
    def __init__(self,id) -> None:
        self.id = id
        self.youOwn = {}        #People should give you this amount
        self.theyOwn = {}       #You should give this amount to people


    def updateYouOwn(self,user_id,amount) :
        
        if user_id in self.theyOwn.keys():
            if self.theyOwn[user_id] >= amount:
                self.theyOwn[user_id] = self.theyOwn[user_id] - amount
                return 
            else:
                amount =  amount - self.theyOwn[user_id]
                self.theyOwn[user_id] = 0

        if user_id in self.youOwn.keys():
            self.youOwn[user_id] += amount
        else :
            self.youOwn[user_id] = amount
    
    def updateTheyOwn(self,user_id,amount):
        
        if user_id in self.youOwn.keys():
            if self.youOwn[user_id] >= amount:
                self.youOwn[user_id] = self.youOwn[user_id] - amount
                return
            else:
                amount -= self.youOwn[user_id]
                self.youOwn[user_id] = 0
        
        if user_id in self.theyOwn.keys():
            self.theyOwn[user_id] += amount
        else :
            self.theyOwn[user_id] = amount
        
        # print("User :",self.id," theyOwn : " , self.theyOwn)

