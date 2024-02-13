let count_value = new Promise((resolve, reject)=>{
    resolve("Promise Done")
})

count_value.then(function success_code(result) {
    console.log("first promise")
}).then(function another_success_code() {
    console.log("another promise")
}).then(function yet_another_success_code() {
    console.log("yet another promise")
})