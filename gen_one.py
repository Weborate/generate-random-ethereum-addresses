from eth_account import Account


# generate addresses for testing addWL()
acc = Account.create()
print('Address:', acc.address)
print('Key:', acc.key.hex())
