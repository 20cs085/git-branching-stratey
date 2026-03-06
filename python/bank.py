class Account:
	def __init__(self, name ,balance,min_balance):
		self.name = name 
		self.balance = balance 
		self.min_balance = min_balance
	
	def deposite(self , amount):
		self.balance += amount

	def withdraw(self, amount):
		if self.balance - amount >= min_balance:
			self.balance -= amount
		else:
			print('Sorry , Insufficient Funds')
	
	def printStatement(self):
		print('Account Balance:',self.balance)

class SavingsAccount(Account):
	def __init__(self,name , balance):
		super().__init__(name,balance,0)
	def __str__(self):
		return "It is {}'s Savings Account with Balance:{}".format(self.name,self.balance)


class CurrentAccount(Account):
	def __init__(self,name , balance):
		super().__init__(name,balance,-10000)
	def __str__(self):
		return "It is {}'s Savings Account with Balance:{}".format(self.name,self.balance)

s=SavingsAccount('Sahithya',10000)
print(s)
s.deposit(5000)
s.printStatement()
s.withdraw(12000)
s.printStatement()



