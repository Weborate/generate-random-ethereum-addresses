from eth_account import Account


# generate addresses for testing addWL()

for x in range(1000):
    acct = Account.create()
    print(acct.address + ', ')