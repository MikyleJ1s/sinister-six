console.log("Using javascript...")
var x = 10; var y = 4
operators = {'+': (x+y),'-': (x-y),'*': (x*y),'/': (x/y), '%': (x%y)}
for (var i in operators){
    if (y == 0 && (i == '/' || i == '%')){
        console.log(x + i + y + ' is not possible')
    }
    else{
        console.log(x + i + y + '=' + operators[i])
    }
    
}