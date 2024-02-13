function display(data){
    document.getElementById("result").innerHTML = data
}

display("Mikyle")

let my_promise = new Promise((success, error) => {
    // normal code to be executed ...
    let value = 0
    if (value === 0){
        success("Succesfully")
    }
    else{
        error("Unsuccesful")
    }
})

// now calling the promise ...
my_promise.then(
    // when the promise is successfully executed ... 
    function(value){
        display(value)},
    function(error){
        display(error)
    }
        
    )

// let my_other_promise = new Promise(function(success, error){

// })

