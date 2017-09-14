
accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist


def name_and_balance(item):
    for certain_acc in item:
        if transfer_from == certain_acc['account_number']:
            print("Welcome " + str(certain_acc['client_name']) + "! Your current balance is: " + str(certain_acc['balance']))
            account_number_check(item)
            return
    print("The account number you entered is invalid.")


def account_number_check(item):
    for certain_acc in accounts:
        if transfer_from == certain_acc['account_number']:
            transfer_address_check(item)
            return 
    print("The number you inserted is invalid. Please try again!")


def transfer_address_check(item):
    transfer_to = int(input("Please provide the account number to which you want to transfer money!: "))
    for certain_acc in accounts:
        if transfer_to == transfer_from:
            print("You cannot transfer money to your own account. Please enter an other account number!")
            return
        elif transfer_to == certain_acc['account_number']:
            vertify_amount(transfer_to)
            return
    print("The transfer address number you inserted is invalid. Please try again!")


def vertify_amount(transfer_to):
    amount = int(input("How much money do you want to transfer? "))
    for certain_acc in accounts:
        if transfer_from == certain_acc['account_number'] and certain_acc['balance'] >= amount:
            transfer(transfer_to, amount)
            return
    print("You don't have enough money on your account.")


def transfer(transfer_to, amount):
    for certain_acc in accounts:
        if certain_acc['account_number'] == transfer_from:
            certain_acc['balance'] -= amount
        if certain_acc['account_number'] == transfer_to:
            certain_acc['balance'] += amount
    end_message(transfer_to, amount)


def end_message(transfer_to, amount):
    for certain_acc in accounts:
        if certain_acc['account_number'] == transfer_from:
            From = certain_acc
        if certain_acc['account_number'] == transfer_to:
            to = certain_acc
    print("The transfer is complete! Your current account balance is: " + str(From['balance']) + "\n Thank you for your transaction! We hope to see you again soon!")


transfer_from = int(input("Please provide your account number!: "))
name_and_balance(accounts)
