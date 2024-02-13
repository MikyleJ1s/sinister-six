const express = require('express')

// create express application on the app variable ...
const app = express()

// used for reading the json data ...
app.use(express.json())

const customers = require('./customers.json')

app.get('/', (req, res)=>{
    res.send("Welcome to ExpressJS example")
})

app.get('/api/customers', (req, res)=>{
    res.send(customers)
})

app.post('/api/insertcustomer', (req, res)=>{
    const new_customer = {
        customer_id: customers.length + 1, 
        customer_name: req.body.customer_name}
    // push the above customer object into the cutomer array ...
    customers.push(new_customer)
    res.send(new_customer)
})

// retrieve customer using the customer id and display it ...
app.get('/api/getcustomer/:id', (req, res)=>{
    const customer = customers.find(customer => customer.customer_id === parseInt(req.params.id))
    // if there is no such customer then display an error ...
    if (!customer){
        res.status(404).send('<h2>Customer not found</h2>')
    }
    res.send(customer)
})

// delete customer using their id ...
app.delete('/api/deletecustomer/:deleteid', (req, res)=>{
    const customer = customers.find(customer => customer.customer_id === parseInt(req.params.deleteid))
    if (!customer){
        res.status(404).send('<h2>No such customer</h2>')
    }
    const index = customers.indexOf(customer)

    // splice to remove the customer from the array ... 
    customers.splice(index, 1)
    res.send(customer)
})

app.put('/api/updatecustomer/:id', (req, res)=>{
    const customer = customers.find(customer => customer.customer_id === parseInt(req.params.id))
    // if there is no such customer then display an error ...
    if (!customer){
        res.status(404).send('<h2>Customer not found</h2>')
    }
    customer.customer_name = req.body.customer_name
    res.send(customer)
})

// port environment variable ... 
const port = process.env.PORT || 8080
app.listen(port, ()=>console.log(`Listening to port number ${port}`))