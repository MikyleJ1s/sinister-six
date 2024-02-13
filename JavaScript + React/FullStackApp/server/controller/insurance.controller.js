const mysql = require('mysql')

const connection = mysql.createConnection({
    host: 'localhost', 
    user: 'root', 
    password: 'Mikyle123', 
    database: 'fullstackapp'
})

connection.connect((error)=>{
    if (error) throw error
    console.log('connected to database')
})

exports.insertInsurance = (req, res) => {
    if (!req.body.insuranceName){
        return res.status(400).send({message: 'come on bro, just put in an insurance name'})
    }
    var insuranceData = req.body
    console.log(insuranceData)

    connection.query("insert into insurance set ? ", insuranceData, function(error, result, fields){
        if (error) throw error
        return res.send({data: result, message: 'new insurance inserted successfully'})        
    })
}


// retrieve all employees ...
exports.selectAllInsurances = (req, res)=>{
    connection.query("select * from insurance", 
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// get employee by their id ...
exports.selectInsurance = (req, res)=>{
    connection.query("select * from insurance where insuranceID = ?", 
    [req.params.i_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// get employee by their name ...
exports.selectInsuranceWithName = (req, res)=>{
    connection.query("select * from insurance where insuranceName = ?", 
    [req.params.i_name],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// update an employee ...
exports.updateInsurance = (req, res)=>{
    if (!req.body.insuranceName){
        return res.status(404).send({
            message: "Insurance Name can't be Empty"
        })
    }    
    connection.query("update insurance set insuranceName = ?, insurancePremium = ?, insuranceAgeLimit = ? where insuranceID = ?", 
    [req.body.insuranceName, req.body.insurancePremium, req.body.insuranceAgeLimit, req.params.i_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}

// delete an employee ...
exports.deleteInsurance = (req, res)=>{   
    connection.query("delete from insurance where insuranceID = ?", 
    [req.params.i_id],
    function(error, result, fields){
        if (error) throw error;
        return res.send(JSON.stringify(result))
    })
}
