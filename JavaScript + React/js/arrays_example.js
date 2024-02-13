// combining arrays ...
fruit = ["banana", "apple", "kiwi", "grapes", "mango"]
vegetable = ["potato", "lettuce", "cucumber"]

console.log(fruit.concat(vegetable))

// write a javascript program to sum all the even numbers in the given array
given_numbers = [2, 7, 8, 10, 11, 13]
total = 0
for (let x of given_numbers){
    if (x % 2 == 0){
        total += x
    }
}
console.log(total)

// pushing an element into an array ... 
fruit.push("watermelon")
console.log(fruit)

// poping an element from an array ...
vegetable.pop()
console.log(vegetable)

// removing an element from the front ...
vegetable.shift()
console.log(vegetable)

// adding an element to the front ...
fruit.unshift("orange")
console.log(fruit)

// to add new elements anywhere into the array ...
fruit.splice(3, 0, "lime", "strawberry") 
console.log(fruit)

// removing elements permanently using splice ... 
fruit.splice(3, 2) 
console.log(fruit)

// removing element temperarily using slice ...
f = fruit.slice(5)
console.log(f)

// sort the elements ...
fruit.sort()
console.log(fruit)

// reverse an array ...
console.log(fruit.reverse())

// sort the integer elements ...
values = [3, 5, 1, 4, 2]
values.sort(function (x, y){
    return x - y})
console.log(values)

for (const i in given_numbers){
    console.log(given_numbers[i])
}

