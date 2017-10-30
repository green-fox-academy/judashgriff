class Animal {
        
    constructor(type) {
        hunger = 5, 
        thirst = 5, 
        eat = function() {
            this.hunger -= 1;
        };
        drink = function() {
            this.thirst -= 1;
        };
        play = function() {
            this.hunger++
            this.thirst++
        };
    }
}

class Farm { 
    constructor(type) {
        freeSlots = 0,
        animals = ["animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal", "animal"]
        breed = function() {
            if (this.freeSlots > 0) {
                this.animals.push("animal")
            }
        }
        slaughter = function() {

        }
    }
}

const SheepFarm = new Farm(20)

