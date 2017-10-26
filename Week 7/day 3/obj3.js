'use strict';

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.

let acc = function(accounts) {
    let account = [];
    accounts.forEach(function(client) {
        account[client.client_name] = client.balance
    })
    return account;
}

let transfer_check = function(from, to, amount) {
    if (check_acc(from) === true && check_acc(to) === true) {
        transfer(from, to, amount);
    } else {
        console.log("404 - account not found")
    }
}

let check_acc = function(acc) {
    let isValid = false;
    accounts.forEach(function(client) {
        if (client.account_number === acc) {
        isValid = true;
        } 
   }) 
   return isValid;
}



let transfer = function(from, to, amount) {
    accounts.forEach(function(client) {
        if (client.account_number === from) {
            if (client.balance >= amount) {
                subtract(from, to, amount);
            } else {
                return "Not enough money!"
            }
        }
    })
}

let subtract = function(from, to, amount) {
    accounts.forEach(function(client) {
        if (client.account_number === from) {
            client.balance -= amount;
            add(from, to, amount)
        }
    })
}

let add = function(from, to, amount) {
    accounts.forEach(function(client) {
        if (client.account_number === to) {
            client.balance += amount;
            commit(from, amount)
        }
    })
}

let commit = function(from, amount) {
    accounts.forEach(function(client) {
        if (client.account_number === from) {
            console.log(amount + " has been sent from " + client.client_name + "\'s account. The new balance is " + client.balance)
        }
    })
}

transfer_check(43546731, 23456311, 5000000)

console.log(acc(accounts));