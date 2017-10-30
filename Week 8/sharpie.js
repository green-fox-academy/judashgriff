let Sharpie = {
    color: "red",
    width: 6,
    inkAmount: 100,
    use: function(){
        this.inkAmount -= this.width;
        console.log(this.inkAmount);
    }
}

let reddish = Sharpie
let useCounter = 0;
for (i = reddish.inkAmount; i > reddish.width; i -= reddish.width) {
    reddish.use();
    useCounter++
}
console.log(useCounter);