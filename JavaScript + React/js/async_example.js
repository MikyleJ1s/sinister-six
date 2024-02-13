// using only async ... 
async function func(){
    console.log("Async Function")
    return Promise.resolve("Promise returned using an async function")
}

func().then(function(result){console.log(result)})

// now using async and await ...

// create a promise ...
let promise = new Promise((resolve, reject)=>{
    setTimeout(() => {
        resolve("Promise Resolved")    
    }, 5000);
})

// async function ...
async function asyncFunction(){
    let result = await promise
    console.log(result)
    if (result == 1){
        console.log("Promise Complete")
    }else{console.log("Promise Incomplete")}
}

// calling the async function ...
asyncFunction()