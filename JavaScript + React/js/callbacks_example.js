// normal function ...
function greetings(name) {
    console.log("Hello " + name)
}

// callback example ...
function welcome(message, function_name) {
    console.log(message)
    function_name("John")
}

greetings("Mikyle")

welcome("Welcome", greetings)


