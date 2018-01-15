'use strict'

// 10.
// Create a function that takes an array of integers and returns the average of the even numbers from that array

const arrayOfIntegers = [-4,0,1,2,3,4,5,6,7,8,9,10,30];

function seeIfEven(num) {
    return (num % 2 === 0);
}

function countEvensAverage(array) {
    const evens = arrayOfIntegers.filter(seeIfEven);
    let sum = 0;
    evens.forEach((element) => {
        sum += element;
    });
    return (sum / evens.length);

}

const resultOfFinalExamExercise = countEvensAverage(arrayOfIntegers);

// console.log(resultOfFinalExamExercise);
