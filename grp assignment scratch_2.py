class Bank (object):
    def super__init__(self, bankid, name, location):
        # Represents the bank
        self.bankid = bankid
        self.name = name
        self.location = location
        pass
    class Teller:
        def super__init__(self):
            self.amount = amount

        def __init__(self, accounts, name):
            self.accounts = accounts
            self.name = name

            print("{bankname} bank was just created".format(bankname=name))

        def collectmoney(self, person, amount):
            self.person = person
            self.amount = amount

            print "{personname} withdrew ${amount} from {bankname}"
            personname = person.name
            amount = self.amount
            bankname = self.name

        def openaccount(self, person):
            self.accounts[person.name] = 0

            print(
                "{personname}, thanks for opening an account at{CHE}!.format(personname = person.name, bankname = self.name)")

        def closeaccount(self, name, Id):
            self.name = 0
            self.Id = Id
            pass
        def loanrequest(self, name, Id, amount, security):
            self.name = name
            self.Id = Id
            self.amount = amount
            self.security = security

            if not (person.name in self.accounts.keys()):
                print"{name} does not have an account in {bank}'.'format(name = person, bank = self.name)"
               return
            self.accounts[person.name] -= amount
            person.money += amount
            if self.accounts[person.name] - amount < 1000,000:
                print
                "{personname} does not have enough money in the account to inquire for a loan ${amount:.0f}.".format(
                    personname=person.name, amount=amount)
                return
            self.accounts[person.name] -= amount

        def provideinfo(self):
            pass
        def issuecard(self):
            pass
    class Customer(Teller):
        def super__init__(self, Id, name, address, phoneno, accountno):
            self.Id = Id
            self.name = name
            self.address = address
            self.phoneno = phoneno
            self.accountno = accountno
            pass

        def __init_subclass__(cls, **kwargs):

        def generalinquiry(self, name):
            pass
        def depositmoney(self, person, amount, Id):
            self.person = person
            self.amount = amount
            self.Id = Id

        def withdrawmoney(self, person, amount):
            self.person = person
            self.amount = amount
            if self.accounts[person.name] - amount < 0:
                print "{personname} does not have enough money in the account to withdraw ${amount:.0f}.".format(personname = person.name, amount = amount)
                return
            self.accounts[person.name] -= amount
            person.money += amount

            print "{personname} withdrew ${amount} from {bankname}. {personname} has ${personmoney}. {personname}'s account has ${accountmoney}.".format(personname = person.name, amount = amount, bankname = self.name, personmoney = person.money, accountmoney = self.accounts[person.name])
            pass
        def openaccount(self, name, nationalid, phoneno):
            self.name = name
            self.nationalid = nationalid
            self.phoneno = int

        def closeaccount(self):
            pass
        def applyforloan(self, name, amount, date):
            self.name = name
            self.amount = amount
            self.date = str

        def requestcard(self):
            pass
        class Account():
            def __init__ (self, Id, customerid):
                self.Id = Id
                self.customerid = customerid
                pass
            class loan():
                def __init__ (self, Id, type, accountid, customerid):
                 self.Id = Id
                 self.type = type
                 self.accountid = accountid
                 self.customerid = customerid
                 pass
            class checking(account):
                def __init__(self, Id, customerid):
                    self.Id = Id
                    self.customerid = customerid
            class savings (account):
                def __init__(self, Id, customerid):
                    self.Id = Id
                    self.customerid = customerid





