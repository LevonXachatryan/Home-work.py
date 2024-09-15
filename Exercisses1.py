
from abc import ABC,abstractmethod
from typing import List


class Account(ABC):
    def __init__(self, account_number: int, balance: float, account_type: str):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
    
    @abstractmethod
    def deposit(self, amount: float) -> None:
        """Deposit money"""
        pass
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Withdraw money"""
        pass
    
    @abstractmethod
    def transfer(self, destination: 'Account', amount: float) -> None:
        """Transfer money"""
        pass
    
    @abstractmethod
    def show_balance(self) -> None:
        pass
    
    @abstractmethod
    def get_account_type(self) -> str:
        """Return the type of account."""
        pass
    
class CheckingAccount(Account):
    def __init__(self,  account_number: int, balance: float, overdraft_limit: float):
        super().__init__(account_number, balance, "Checking")
        self.overdraft_limit = overdraft_limit
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if self.balance < amount:
            raise ValueError("Pass")
        self.balance -= amount

    def transfer(self, destination: Account, amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        
    def show_balance(self) -> None:
        print(f"Checking Account Balance: ${self.balance: .2f}")
        
    def get_account_type(self) -> str:
        return "Checking"
        
class SavingsAccount(Account):
    def __init__(self,  account_number: int, balance: float, interest_rate: float):
        super().__init__(account_number, balance, "Savings") 
        self.interest_rate = interest_rate
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if self.balance < amount:
            raise ValueError("Pass")
        self.balance -= amount
        
    def transfer(self, destination: Account, amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        
    def show_balance(self) -> None:
        print(f"Checking Account Balance: ${self.balance: .2f}")
    
    def get_account_type(self) -> str:
        return 'Savings'

class JointAccount(Account):
    def __init__(self, account_number: int, balance: float, joint_owners: List[str]):
        super().__init__(account_number, balance, 'Joint')
        self.joint_owners = joint_owners
        
    def deposit(self, amount: float) -> None:
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if self.balance < amount:
            raise ValueError("Pass")
        self.balance -= amount

    def transfer(self, destination: Account, amount: float) -> None:
        self.withdraw(amount)
        destination.deposit(amount)
        
    def show_balance(self) -> None:
        print(f"Checking Account Balance: ${self.balance:}")
    
    def get_account_type(self) -> str:
        return 'Joint'

class TransactionManager(ABC):
    @abstractmethod
    def log_transaction(self, transaction_type: str, amount: float) -> None:
        pass
    
    @abstractmethod
    def show_transaction_history(self) -> None:
        pass

class Transaction():
    def __init__(self, from_account: Account, to_account: Optional[Account], amount: float, transaction_type: str):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.transaction_type = transaction_type
        
        
    def log(self) -> None:
        print(f"Transaction: {self.transaction_type}")

class Customer():
    def __init__(self, name: str, contact_info: str, accounts: List[Account]):
        self.name = name
        self.contact_info = contact_info
        self.accounts = []
        
    def add_account(self, account: Account) -> None:
        pass
    
    def view_accounts(self) -> None:
        pass
    
    def view_transaction_history(self) -> None:
        pass