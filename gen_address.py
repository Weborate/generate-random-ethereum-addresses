from eth_account import Account


# generate addresses for testing addWL()
addresses = []
for x in range(1000):
    acct = Account.create()
    addresses.append(acct.address)
print(','.join(addresses))