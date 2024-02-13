// normal function ...
function displayNormal(){
    document.write("<h1>Welcome. I am using a normal function in javascript.</h1>")
}

// function expression ...
let displayExpression = function(){
    document.write("<h2>Welcome. I am using a function expression in javascript.</h2>")
}

// arrow function ...
let displayArrow = () => {
    document.write("<h3>Welcome. I am using an arrow function in javascript.</h3>") // curly brackets not needed if there is only one line ...
}

var stringValues = ['earth', 'heart', 'dad', 'medicine', 'mom']
number_of_palindromes = 0

let is_a_palindrome = () => {
    for (let word of stringValues){
        if (word.split('').reverse().join('') === word){
            number_of_palindromes += 1
        }
    }
    
    return number_of_palindromes // returns 2 since "dad" and "mom" are palindromes ...
}

console.log(is_a_palindrome())

const numbers = [5,6,15,20,16,9]

function cube(n){
    return n*n*n
}

const cubes = numbers.map(cube)
console.log(cubes) 

// filter even numbers from an array ...
const evens = numbers.filter(value => value % 2 == 0)
console.log(evens)

names = ['mikyle', 'kyle', 'neville', 'vukosi', 'desiree', 'sindiswa', 'lindani', 'emmanuel', 'swapna', 'ria', 'handsome', 'anita', 'taswell', 'marcello']
console.log(names.filter(value => value.endsWith("e")))

// Take an array of 10 elements and split it into middle and store the elements in to two different arrays
const full_array = [1, 2, 3, 4, 5, 6, 7]
var first_half = []
var second_half = []

var i = 0
for (let index = 0; index < Math.floor(full_array.length / 2); index++) {
    first_half[i] = full_array[index];
    i++
}

var i = 0
for (let index = Math.floor(full_array.length / 2); index < full_array.length; index++) {
    second_half[i] = full_array[index];
    i ++
}

console.log(full_array)
console.log(first_half)
console.log(second_half)


// Take 20 integer values in the array and print number of positive,number of negative,number of odd and number of even and number of 0s in the above values
array = [5, 8, -3, 13, 15, -2, 18, -1, -7, 0, 1, 2, 3, 0, 8, 0, 0, 8, -17, -1]
console.log('Original: ' +array)
console.log('Positives: '+(array.filter(value => value >= 0)).length)
console.log('Negatives: '+(array.filter(value => value < 0)).length)
console.log('Odds: '+(array.filter(value => value % 2 !== 0)).length)
console.log('Evens: '+(array.filter(value => value % 2 === 0)).length)
console.log('Zeros: '+(array.filter(value => value === 0)).length)