const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += amt; 
        this.cash -= amt * (this.tax.slice(0, -1) / 100);
        console.log(this.name + " got " + amt + " money.")
    }
}

const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += amt; 
        this.cash -= amt * (this.tax.slice(0, -1) / 100);
        console.log(this.name + " got " + amt + " money.")
    }
}

const Shuffler = {
    cash: 10000,
    count: 0,
    pick: function() {
        let choice = Math.floor(Math.random());
        if (this.count % 2 === 0) {
            Panama.deposit(1000);
        } else {
            Cyprus.deposit(1000);
        }
        this.count += 1;
    }
}

Shuffler.pick()
Shuffler.pick()
Shuffler.pick()

console.log( Panama.cash )
console.log( Cyprus.cash )