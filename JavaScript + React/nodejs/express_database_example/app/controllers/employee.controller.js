// import mysql ...
const mysql = require('mysql') // import mysql2 later if this decides to not work anymore 

// establish the database connection ...
const connection = mysql.createConnection({
    host: 'localhost', 
    user: 'root',
    password: 'Mikyle123',
    database: 'expressexample'
})

// connect to the databse ...
connection.connect((err)=>{
    if (err) throw err
    console.log("Connected to MySQL Database")
})

// insert an employee into the database ...
exports.createEmployee = (req, res) => {
    // validate request ...
    if (!req.body.employeeName){
        return res.status(404).send({
            message: "Employee Name can't be Empty"
        })
    }    

    var emptyData = req.body
    console.log(emptyData)

    // connect with the database and insert the employee ...
    connection.query("insert into employee set ? ",emptyData, function(error, result, fields){
        if (error) throw error;
        return res.send({
            data: result, 
            message: 'New Employee was Added'
        })
    })
}

// retrieve all employees ...
exports.selectAllEmployees = (req, res)=>{
    connection.query("select * from employee", 
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// get employee by their id ...
exports.selectEmployee = (req, res)=>{
    connection.query("select * from employee where employeeID = ?", 
    [req.params.e_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// get employee by their name ...
exports.selectEmployeeWithName = (req, res)=>{
    connection.query("select * from employee where employeeName = ?", 
    [req.params.e_name],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// update an employee ...
exports.updateEmployee = (req, res)=>{
    if (!req.body.employeeName){
        return res.status(404).send({
            message: "Employee Name can't be Empty"
        })
    }    
    connection.query("update employee set employeeName = ?, employeeSalary = ?, employeeDept = ? where employeeID = ?", 
    [req.body.employeeName, req.body.employeeSalary, req.body.employeeDept, req.params.e_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// delete an employee ...
exports.deleteEmployee = (req, res)=>{   
    connection.query("delete from employee where employeeID = ?", 
    [req.params.e_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}
