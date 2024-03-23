'''
  Practical Test 4

  testAccounts.py - program to test functions of accounts.py
  
  Student Name   :
  Student Number :
  Date/prac time :
'''
from accounts import BankAccount, Portfolio, InsufficientFundsError, AccountNotFoundError

print('\n<--- Bank Accounts Portfolio --->\n')
myAccounts = Portfolio()

# add code for tasks here
#add accounts

myAccounts.addAccount("Castle", "999999-1", 1000)
myAccounts.addAccount("Shrubbery", "999999-2", 100)
myAccounts.addAccount("Grail", "999999-3", 100)
#desposit/Withdraw

#myAccounts.deposit("Castle",100)
#myAccounts.withdraw("Shrubbery", 10)
#myAccounts.withdraw("Shrubbery", 1000)
#myAccounts.withdraw("Grail", 1000)

myAccounts.deposit("Castle",100)

try:
    myAccounts.withdraw("Shrubbery", 10)
except InsufficientFundsError as e:
    print(e)

try:
    myAccounts.withdraw("Shrubbery", 1000)
except InsufficientFundsError as e:
    print(e)

try:
    myAccounts.withdraw("Grail", 1000)
except InsufficientFundsError as e:
    print(e)
except AccountNotFoundError as e:
    print(e)

#e.g.
#myAccounts.addAccount("Everyday", "1111-007", 1000)
#myAccounts.deposit("Everyday",200)
#print(myAccounts)
myAccounts.withdraw("Castle", 100)

print(myAccounts.getNumAccounts())
print(myAccounts.getTotalBalance())
myAccounts.balances()
