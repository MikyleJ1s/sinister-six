module.exports = (app) => {
    const employeeController = require('../app/controllers/employee.controller.js')
    // create a new employee ... 
    app.post('/employees', employeeController.createEmployee)
    // select all employees
    app.get('/getallemployees', employeeController.selectAllEmployees)
    // select employee by id ...
    app.get('/getemployee/:e_id', employeeController.selectEmployee)
    // select employee by name ...
    app.get('/getemployeename/:e_name', employeeController.selectEmployeeWithName)
    // update employee ...
    app.put('/updateemployee/:e_id', employeeController.updateEmployee)
    // delete employee ...
    app.delete('/deleteemployee/:e_id', employeeController.deleteEmployee)

}