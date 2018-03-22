'use strict'

// 10.
// Create a function that takes an array of integers and returns the average of the even numbers from that array

const arrayOfIntegers = [-4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30];

function seeIfEven(num) {
    return (num % 2 === 0);
}

// function countEvensAverage(array) {
//     const evens = arrayOfIntegers.filter(num % 2 === 0);
//     let sum = 0;
//     evens.forEach((element) => {
//         sum += element;
//     });
//     return (sum / evens.length);
// }

// const resultOfFinalExamExercise = countEvensAverage(arrayOfIntegers);

// console.log(resultOfFinalExamExercise);


function alternateCountEvensAverage(array) {
    const evens = [];
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            evens.push(array[i]);
        }
    }
    let sum = 0;
    for (let i = 0; i < evens.length; i++) {
        sum += evens[i];
    }
    return (sum / evens.length);
}

console.log(alternateCountEvensAverage(arrayOfIntegers));
