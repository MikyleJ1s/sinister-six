const express = require('express')
const cors = require('cors')

const app = express()

app.use(express.json())
//app.use(express.urlencoded({extended: true}))
require('./app/routes.js')(app)

app.get('/', (req, res) => {
    res.json({'message': 'got none for u here lil bro'})
})

app.listen(4300, () => {
    console.log('listening to the server port')
})