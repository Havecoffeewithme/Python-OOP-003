
class Funds:
    
    total_expenses = 0
    total = 0 
    
    error = "";
    
    def __init__(self, total):
        self.total = total
     
     
    # keep track of the money we have spend 
    def set_expense(self, expense):
        # checks if we have enouh money left to spend
        if self.get_funds_left() > expense :
            self.total_expenses += expense
            return True
        
        # failed expense deduction
        self.error = " Out of funds"
        return False
        
    
    # calculates the amount of money we left with
    def get_funds_left(self):
        return self.total - self.total_expenses
    
    
    # return the errors 
    def get_error(self):
        return self.error
    

funds = Funds(100)

if not funds.set_expense(10):
    print(funds.get_error())
    

if not funds.set_expense(200):
    print(funds.get_error())
    
    
# Prints the amount left to screen
print('You have $' + str(funds.get_funds_left()) + ' left.')
    
    
    