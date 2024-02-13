var fs = require('fs'); //importing the file system which is predefined package in node

var data = fs.readFileSync('sample.txt','utf8'); //reading the file synchronously until end of file    
console.log(data);

fs.readFile('sample.txt',function(err,data){
    console.log(data.toString());});
    
// write into the file ...
fs.writeFile('sample.txt','new content added to the file ',function(){
    console.log("write operation completed...")})

// append into the file ...
fs.appendFile('sample.txt','more content added to the file again',function(){
    console.log("append operation completed...")})